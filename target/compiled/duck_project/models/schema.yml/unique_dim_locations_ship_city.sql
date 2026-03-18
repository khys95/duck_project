
    
    

select
    ship_city as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_locations"
where ship_city is not null
group by ship_city
having count(*) > 1


