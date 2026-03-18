import duckdb
import seaborn as sns
import matplotlib.pyplot as plt

con = duckdb.connect("./analytics.duckdb")

# print(con.execute("SELECT * FROM dim_products WHERE quantity>0 ORDER BY quantity DESC").fetchdf())
# print(con.execute("DESCRIBE dim_products").fetchdf())
#
# print(con.execute("SELECT * FROM dim_shippings").fetchdf())
# print(con.execute("DESCRIBE dim_shippings").fetchdf())
#
# print(con.execute("SELECT * FROM dim_promotions").fetchdf())
# print(con.execute("DESCRIBE dim_promotions").fetchdf())

# print(con.execute("SELECT * FROM dim_locations").fetchdf())
# print(con.execute("DESCRIBE dim_locations").fetchdf())
#
# print(con.execute("SELECT * FROM dim_dates ORDER BY quarter").fetchdf())
# print(con.execute("DESCRIBE dim_dates").fetchdf())

# revenuePerMonth = con.execute("SELECT dd.year, dd.month_name, sum(fo.order_total) AS revenue "
#                             "FROM fct_orders fo "
#                             "JOIN dim_dates dd ON fo.date_fk = dd.date_pk "
#                             "GROUP BY dd.year, dd.month_name "
#                             "ORDER BY revenue DESC").fetchdf()
# print(revenuePerMonth)
# # sns.lineplot(data=revenuePerMonth, x="month_name", y="revenue")
# # plt.show()

#Revenue per city
print("----- Revenue per city")
cityRevenue = con.execute("SELECT dl.city, sum(fo.order_total) AS revenue "
                            "FROM fct_orders fo "
                            "JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                            "GROUP BY dl.city "
                            "HAVING revenue > 0 "
                            "ORDER BY revenue DESC ").fetchdf()
print(cityRevenue)
# sns.lineplot(data=cityPopular, x="city", y="revenue")
# plt.show()

#Popular styles and categories in the city of Mumbai.
print("----- Popular styles and categories in the city of Mumbai")
popular = con.execute("SELECT style, category, count(*) AS popularity "
                        "FROM fct_orders fo "
                        "JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                        "JOIN dim_products dp ON fo.product_fk = dp.product_pk "
                      "WHERE city='mumbai' "
                      "GROUP BY category, style, city "
                      "HAVING popularity > 1 "
                      "ORDER BY popularity DESC LIMIT 50").fetchdf()
print(popular)

#Order popularity by month.
print("----- Order popularity by month")
monthtrend = con.execute("SELECT month_name, category, count(*) AS popularity "
                        "FROM fct_orders fo "
                        "JOIN dim_dates ds ON fo.date_fk = ds.date_pk "
                        "LEFT JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                        "LEFT JOIN dim_products dp ON fo.product_fk = dp.product_pk "
                        "GROUP BY month_name, category "
                        "HAVING popularity > 1 "
                        "ORDER BY month_name, popularity desc").fetchdf()
print(monthtrend)