
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select style
from "analytics"."main"."dim_products"
where style is null



  
  
      
    ) dbt_internal_test