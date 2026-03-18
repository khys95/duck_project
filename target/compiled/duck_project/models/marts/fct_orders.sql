-- SELECT order_id, customer_id, amount FROM "analytics"."main"."stg_orders"
-- WHERE status = 'completed'

-- SELECT date, ship_city, ship_state, category
-- FROM "analytics"."main"."stg_orders"
-- WHERE ship_city = 'mumbai'
-- LIMIT 10

-- SELECT ship_city, COUNT(*) AS count_city
-- FROM "analytics"."main"."stg_orders"
-- GROUP BY ship_city
-- ORDER BY COUNT(*) DESC

SELECT *
FROM "analytics"."main"."stg_orders"