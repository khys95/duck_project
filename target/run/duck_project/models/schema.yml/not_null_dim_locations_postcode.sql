
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select postcode
from "analytics"."main"."dim_locations"
where postcode is null



  
  
      
    ) dbt_internal_test