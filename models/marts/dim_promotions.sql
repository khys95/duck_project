SELECT
    index AS promotion_pk,
    promotions,
    sales_channel
FROM {{ ref('stg_orders')}}