
  
  create view "analytics"."main"."dim_shippings__dbt_tmp" as (
    SELECT
    index AS shipping_pk,
    shipment_status,
    fulfillment,
    shipping_rate,
    courier_status,
    fulfilled_by
FROM "analytics"."main"."stg_orders"
  );
