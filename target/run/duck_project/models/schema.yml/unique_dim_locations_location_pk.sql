
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    location_pk as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_locations"
where location_pk is not null
group by location_pk
having count(*) > 1



  
  
      
    ) dbt_internal_test