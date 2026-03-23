#In this file answers regarding revenue can be found

import duckdb
import matplotlib.pyplot as plt
from matplotlib import ticker

con = duckdb.connect("./analytics.duckdb")

#Calculating revenue by subtracting all cancelled orders!
#(NOT all cancelled orders have a quantity equaling to zero!)
print("----- Revenue displayed by amount, quantity and cancelled status")
revenueAll = con.execute("SELECT fo.amount, fo.quantity, ds.shipment_status, sum(fo.order_total) AS revenue "
                            "FROM fct_orders fo "
                            "JOIN dim_shippings ds ON fo.shipping_fk = ds.shipping_pk "
                            "GROUP BY fo.amount, fo.quantity, ds.shipment_status "
                            "HAVING ds.shipment_status = 'cancelled'"
                            "ORDER BY fo.quantity DESC").fetchdf()
print(revenueAll)


#Gross revenue (Includes cancelled orders where quantity is 1 or 2)
print("----- Single number: Gross revenue")
revenueGross = con.execute("SELECT sum(fo.order_total) AS revenue_total "
                            "FROM fct_orders fo ").fetchone()[0]
print(revenueGross)


#Revenue lost to cancelled orders
print("----- Single number: revenue lost to cancelled orders")
revenueCancelled = con.execute("SELECT sum(fo.order_total) AS revenue_cancelled "
                            "FROM fct_orders fo "
                            "JOIN dim_shippings ds ON fo.shipping_fk = ds.shipping_pk "
                            "WHERE ds.shipment_status = 'cancelled'").fetchone()[0]
print(revenueCancelled)


#Actual revenue (EXCLUDES ALL CANCELLED orders)
print("----- Single number: Net revenue")
revenueNet= revenueGross - revenueCancelled
print(revenueNet)


# Revenue per month
print("----- Revenue per month")
revenuePerMonth = con.execute("SELECT dd.month_name, sum(fo.order_total) AS revenue "
                            "FROM fct_orders fo "
                            "LEFT JOIN dim_dates dd ON fo.date_fk = dd.date_pk "
                            "LEFT JOIN dim_shippings ds ON fo.shipping_fk = ds.shipping_pk "
                            "WHERE ds.shipment_status != 'cancelled' "
                            "GROUP BY dd.month_name, dd.month_number "
                            "ORDER BY dd.month_number ASC").fetchdf()
print(revenuePerMonth)

#BOX PLOT
# plt.figure(figsize=(14, 6))
# bars = plt.bar(revenuePerMonth['month_name'], revenuePerMonth['revenue'],
#                color='skyblue', edgecolor='black', alpha=0.8)
#
# plt.ylim(0, max(revenuePerMonth['revenue']) * 1.05)
# plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x):,}'))
# plt.xlabel("Month", fontsize=12)
# plt.ylabel("Revenue", fontsize=12)
# plt.title("Monthly Revenue Trend", fontsize=16)
# plt.xticks(rotation=45)
# plt.grid(True, axis='y', linestyle='--', alpha=0.6)
# plt.tight_layout()
# plt.show()

#LINE PLOT
plt.figure(figsize=(12, 4))

# Plot the line
plt.plot(revenuePerMonth['month_name'],
         revenuePerMonth['revenue'],
         marker='o',
         linewidth=2,
         color='navy',
         markersize=8)

plt.ylim(0, max(revenuePerMonth['revenue']) * 1.05)
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x):,}'))

plt.xlabel("Month", fontsize=12)
plt.ylabel("Revenue", fontsize=12)
plt.title("Monthly Revenue Trend", fontsize=16)

plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


#Revenue per city
print("----- Revenue per city")
revenueCity = con.execute("SELECT dl.city, sum(fo.order_total) AS revenue "
                            "FROM fct_orders fo "
                            "LEFT JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                            "LEFT JOIN dim_shippings ds ON fo.shipping_fk = ds.shipping_pk "
                            "WHERE ds.shipment_status != 'cancelled' "
                            "GROUP BY dl.city "
                            "HAVING revenue > 500000 "
                            "ORDER BY revenue DESC ").fetchdf()
print(revenueCity)
# revenueCity.plot(x="city", y="revenue", title="Revenue Over Time", grid=True)
# plt.show()

plt.figure(figsize=(12, 6))
plt.bar(revenueCity['city'], revenueCity['revenue'], color='skyblue')
plt.ylim(0, 7000000)
plt.yticks(range(0, 7000000, 500000))
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x):,}'))
plt.ylabel("Revenue", fontsize=12)
plt.xticks(rotation=45)
plt.xlabel("City", fontsize=12)
plt.title("Revenue by City")
plt.grid(True, axis='y', linestyle='--')
plt.tight_layout()
plt.show()


#Revenue lost to cancelled orders by city
print("----- Revenue lost to cancelled orders grouped by cities")
revenueCancelledCity = con.execute("SELECT dl.city, sum(fo.order_total) AS revenue "
                            "FROM fct_orders fo "
                            "JOIN dim_shippings ds ON fo.shipping_fk = ds.shipping_pk "
                            "JOIN dim_locations dl ON fo.location_fk = dl.location_pk "
                            "WHERE fo.quantity > 0 "
                            "GROUP BY dl.city, ds.shipment_status "
                            "HAVING ds.shipment_status = 'cancelled'"
                            "ORDER BY revenue DESC "
                            "LIMIT 10").fetchdf()
print(revenueCancelledCity)
plt.figure(figsize=(12, 6))
plt.bar(revenueCancelledCity['city'], revenueCancelledCity['revenue'], color='skyblue')
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{int(x):,}'))
plt.ylabel("Revenue", fontsize=12)
plt.xticks(rotation=45)
plt.xlabel("City", fontsize=12)
plt.title("Cancelled Orders Revenue by City")
plt.grid(True, axis='y', linestyle='--')
plt.tight_layout()
plt.show()