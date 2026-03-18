SELECT
    order_id,
    quantity,
    amount,
    date AS date_fk,
    index AS location_fk,
    index AS product_fk,
    index AS promotion_fk,
    index AS shipping_fk,
    quantity*amount AS order_total
FROM {{ ref('stg_orders')}}