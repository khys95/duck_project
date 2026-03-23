#In this file answers regarding trends can be found

import duckdb
import matplotlib.pyplot as plt
from matplotlib import ticker

con = duckdb.connect("analytics.duckdb")

#Popular styles and categories in the city of Mumbai.
print("----- Popular styles and categories in the city of Mumbai")
popular = con.execute("SELECT style, category, count(*) AS popularity "
                    "FROM fct_orders fo "
                    "JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                    "JOIN dim_products dp ON fo.product_fk = dp.product_pk "
                    "WHERE city='mumbai' "
                    "GROUP BY category, style, city "
                    "HAVING popularity > 1 "
                    "ORDER BY popularity DESC LIMIT 10").fetchdf()
print(popular)
# popular.plot(x="category", y="popularity", title="Popularity over time in Mumbai", grid=True)
# plt.show()

popular['product_label'] = popular['category'] + " - " + popular['style']
popular_sorted = popular.sort_values(by='popularity', ascending=True)
plt.figure(figsize=(12, 6))
bars = plt.barh(popular_sorted['product_label'],
                popular_sorted['popularity'],
                color='lightcoral',
                edgecolor='black',
                alpha=0.8)

max_pop = popular_sorted['popularity'].max()
plt.xlim(0, max_pop * 1.05)  # Add a little padding on the right
plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x):,}'))
plt.xlabel("Popularity", fontsize=12)
plt.ylabel("Product", fontsize=12)
plt.title("Top 10 Most Popular Products in Mumbai", fontsize=16)
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
for i, v in enumerate(popular_sorted['popularity']):
    plt.text(v + max_pop*0.01, i, f"{int(v)}", color='black', va='center', fontsize=8)
plt.tight_layout()
plt.show()


#Order popularity by month.
print("----- Order popularity by month")
monthtrend = con.execute("SELECT month_name, category, count(*) AS popularity "
                        "FROM fct_orders fo "
                        "LEFT JOIN dim_dates ds ON fo.date_fk = ds.date_pk "
                        "LEFT JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                        "LEFT JOIN dim_products dp ON fo.product_fk = dp.product_pk "
                        "GROUP BY month_name, category "
                        "HAVING popularity > 1 "
                        "ORDER BY month_name, popularity desc").fetchdf()
print(monthtrend)