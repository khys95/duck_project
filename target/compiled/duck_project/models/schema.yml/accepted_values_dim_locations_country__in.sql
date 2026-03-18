
    
    

with all_values as (

    select
        country as value_field,
        count(*) as n_records

    from "analytics"."main"."dim_locations"
    group by country

)

select *
from all_values
where value_field not in (
    'in'
)


