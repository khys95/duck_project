
  
  create view "analytics"."main"."dim_promotions__dbt_tmp" as (
    SELECT
    index AS promotion_pk,
    promotions,
    b2b,
    var_unnamed22,
    bol_unnamed24
FROM "analytics"."main"."stg_orders"
  );
