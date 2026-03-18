
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select state
from "analytics"."main"."dim_locations"
where state is null



  
  
      
    ) dbt_internal_test