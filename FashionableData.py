import duckdb
import pandas as pd

#Connect to database, duckDB
con = duckdb.connect("./analytics.duckdb")

con.execute("CREATE SCHEMA IF NOT EXISTS raw")

#Load Fashionable sales report and add low_memory flag to be able to read chucks of different data types in the same column.
df = pd.read_csv("./seeds/report.csv", low_memory=False)
print(df)

#Column cleanup
df.columns = df.columns.str.strip()
df.columns = df.columns.str.replace("-", "_")
df.columns = df.columns.str.replace(" ", "_")
df.columns = df.columns.str.replace(":", "_")
df.columns = df.columns.str.lower()

#Row cleanup
df['date'] = pd.to_datetime(df['date'], format='%m-%d-%y')
df['status'] = df['status'].str.strip().str.lower()
df['category'] = df['category'].str.strip().str.lower().str.replace(" ", "_").str.rstrip(".")
df['ship_city']= df['ship_city'].str.strip().str.lower().str.replace(" ", "_").str.rstrip(".")
df['ship_state']= df['ship_state'].str.strip().str.lower().str.replace(" ", "_").str.rstrip(".")

#Creation of raw.orders_csv table with data from original dataframe
con.execute("""
CREATE OR REPLACE TABLE raw.orders_csv AS 
SELECT *
FROM df""")
print("raw.orders_csv table created or updated")
print("Loaded all data into raw.orders_csv from original dataframe with standardized column names and data entries")

#Simple query to make sure clean data is being read
result = con.execute("SELECT * FROM raw.orders_csv LIMIT 5").fetchdf()
print(result)

#To double-check the data types
schema = con.sql("DESCRIBE raw.orders_csv").df()
print(schema)

