
  
  create view "analytics"."main"."dim_products__dbt_tmp" as (
    SELECT index AS product_pk, order_id, style, sku, category, size, asin, quantity, amount,
FROM "analytics"."main"."stg_orders"
  );
