
  
  create view "analytics"."main"."dim_dates__dbt_tmp" as (
    SELECT DISTINCT
    date AS date_pk,
    EXTRACT(year FROM date) AS year,
    EXTRACT(month FROM date) AS month_number,
    EXTRACT(day FROM date) AS day_number,
    strftime(date, '%B') AS month_name,
    strftime(date, '%A') AS day_name,
    CASE when strftime(date, '%w') in ('0', '6') then true
        else false
    end AS is_weekday,
    EXTRACT(quarter from date) AS quarter
FROM "analytics"."main"."stg_orders"
  );
