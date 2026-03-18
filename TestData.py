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
(1, 101, 10, 'cancelled'),
(2, 102, 20, 'completed'),
(3, 103, 30, 'cancelled'),
(4, 104, 40, 'completed'),
(5, 105, 50, 'cancelled'),
(6, 106, 60, 'completed'),
(7, 107, 70, 'cancelled'),
(8, 108, 80, 'completed'),
(9, 109, 90, 'initiated')
""")

print(con.execute("SELECT * FROM raw_orders").fetchall())