
    
    

select
    product_pk as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_products"
where product_pk is not null
group by product_pk
having count(*) > 1


