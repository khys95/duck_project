
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select ship_city
from "analytics"."main"."dim_locations"
where ship_city is null



  
  
      
    ) dbt_internal_test