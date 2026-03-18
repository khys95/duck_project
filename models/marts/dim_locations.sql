SELECT
    index AS location_pk,
    city,
    state,
    postcode,
    country
FROM {{ ref('stg_orders')}}