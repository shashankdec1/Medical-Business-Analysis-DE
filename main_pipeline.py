from etl.extract import extract_sales, extract_treatments
from etl.transform import transform_data
from etl.load import load_dataframe
from sqlalchemy import create_engine
from config import DB_CONFIG
import pandas as pd


def run_pipeline():

    print("Extracting data from sources...")

    sales = extract_sales()
    treatments = extract_treatments()


    print("Connecting to database...")

    engine = create_engine(
        f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
    )


    # read existing database tables
    try:
        existing_sales = pd.read_sql("SELECT * FROM pharma_sales", engine)
        existing_treatments = pd.read_sql("SELECT * FROM patient_treatments", engine)
    except:
        existing_sales = pd.DataFrame()
        existing_treatments = pd.DataFrame()


    # combine existing + new data
    sales = pd.concat([existing_sales, sales]).drop_duplicates()
    treatments = pd.concat([existing_treatments, treatments]).drop_duplicates()


    print("Transforming data...")

    merged = transform_data(sales, treatments)


    print("Loading data to PostgreSQL...")

    load_dataframe(sales, "pharma_sales")
    load_dataframe(treatments, "patient_treatments")
    load_dataframe(merged, "healthcare_merged")


    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()