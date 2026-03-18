SELECT index AS product_pk, order_id, style, sku, category, size, asin, quantity, amount,
FROM {{ ref('stg_orders')}}
