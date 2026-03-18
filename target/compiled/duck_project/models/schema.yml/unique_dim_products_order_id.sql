
    
    

select
    order_id as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_products"
where order_id is not null
group by order_id
having count(*) > 1


