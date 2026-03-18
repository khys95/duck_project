
    
    

with all_values as (

    select
        city as value_field,
        count(*) as n_records

    from "analytics"."main"."dim_locations"
    group by city

)

select *
from all_values
where value_field not in (
    
)


