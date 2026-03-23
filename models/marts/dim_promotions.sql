SELECT
    index AS promotion_pk,
    promotions,
    sales_channel,
    b2b,
    var_unnamed22,
    bol_unnamed24
FROM {{ ref('stg_orders')}}