
    
    

select
    location_fk as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_products"
where location_fk is not null
group by location_fk
having count(*) > 1


