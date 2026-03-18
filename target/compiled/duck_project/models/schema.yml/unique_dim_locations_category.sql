
    
    

select
    category as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_locations"
where category is not null
group by category
having count(*) > 1


