import pandas as pd

def load_csv_to_table(csv_path, table_name, conn):
    df = pd.read_csv(csv_path)

    # overwrite table to avoid duplicate IDs
    df.to_sql(table_name, conn, if_exists="replace", index=False)

