
import psycopg2
from config import DB_CONFIG

def load_dataframe(df, table):

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for _, row in df.iterrows():
        columns = ",".join(df.columns)
        values = tuple(row)

        query = f"INSERT INTO {table} ({columns}) VALUES %s"
        cur.execute(query,(values,))

    conn.commit()
    cur.close()
    conn.close()
