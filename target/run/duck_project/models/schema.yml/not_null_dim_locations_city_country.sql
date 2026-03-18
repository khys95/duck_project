
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select city, country
from "analytics"."main"."dim_locations"
where city, country is null



  
  
      
    ) dbt_internal_test