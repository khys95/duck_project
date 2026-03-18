
  
  create view "analytics"."main"."stg_orders__dbt_tmp" as (
    SELECT index, order_id, date, status AS shipment_status, fulfilment AS fulfillment, sales_channel,
       ship_service_level AS shipping_rate, style, sku, category, size, asin,
        courier_status, qty AS quantity, currency, amount,
        ship_city AS city, ship_state AS state, ship_postal_code AS postcode,
        ship_country AS country, promotion_ids AS promotions, b2b, fulfilled_by,
        unnamed__22 AS var_unnamed22, unnamed__24 AS bol_unnamed24
FROM raw.orders_csv
  );
