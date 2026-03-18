
    
    

select
    location_pk as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_locations"
where location_pk is not null
group by location_pk
having count(*) > 1


