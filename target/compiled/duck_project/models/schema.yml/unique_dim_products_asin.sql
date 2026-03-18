
    
    

select
    asin as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_products"
where asin is not null
group by asin
having count(*) > 1


