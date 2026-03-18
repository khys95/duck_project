SELECT
    index AS product_pk,
    style,
    sku,
    category,
    size,
    asin,
FROM {{ ref('stg_orders')}}
