#In this file answers regarding the description of tables can be found

import duckdb

con = duckdb.connect("./analytics.duckdb")

print("----- Products dim ")
print(con.execute("SELECT * FROM dim_products").fetchdf())
print(con.execute("DESCRIBE dim_products").fetchdf())

print("----- Shippings dim ")
print(con.execute("SELECT * FROM dim_shippings").fetchdf())
print(con.execute("DESCRIBE dim_shippings").fetchdf())

print("----- Promotions dim ")
print(con.execute("SELECT * FROM dim_promotions").fetchdf())
print(con.execute("DESCRIBE dim_promotions").fetchdf())

print("----- Locations dim ")
print(con.execute("SELECT * FROM dim_locations").fetchdf())
print(con.execute("DESCRIBE dim_locations").fetchdf())

print("----- Dates dim ")
print(con.execute("SELECT * FROM dim_dates ORDER BY quarter").fetchdf())
print(con.execute("DESCRIBE dim_dates").fetchdf())

print("----- Orders fact ")
print(con.execute("SELECT * FROM fct_orders").fetchdf())
print(con.execute("DESCRIBE fct_orders").fetchdf())