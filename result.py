import duckdb

con = duckdb.connect("./analytics.duckdb")

print(con.execute("SELECT * FROM fct_orders").fetchdf())