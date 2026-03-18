
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select category
from "analytics"."main"."dim_locations"
where category is null



  
  
      
    ) dbt_internal_test