
import pandas as pd

def extract_sales():
    return pd.read_csv("object_storage/pharma_sales.csv")

def extract_treatments():
    return pd.read_csv("on_premise/patient_treatments.csv")
