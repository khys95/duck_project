import duckdb

con = duckdb.connect("analytics.duckdb")

con.execute("""
CREATE OR REPLACE TABLE raw_orders (
order_id INTEGER, 
customer_id INTEGER, 
amount DOUBLE,
status VARCHAR
)
""")

con.execute("""
INSERT INTO raw_orders VALUES
(1, 101, 10, 'completEd'),
(2, 102, 20, 'Cancelled'),
(3, 103, 30, 'completed'),
(4, 104, 40, 'initiated'),
(5, 105, 50, 'cAncelled'),
(6, 106, 60, 'completed')
""")

print(con.execute("SELECT * FROM raw_orders").fetchall())