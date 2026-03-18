
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select country
from "analytics"."main"."dim_locations"
where country is null



  
  
      
    ) dbt_internal_test