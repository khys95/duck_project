
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select asin
from "analytics"."main"."dim_products"
where asin is null



  
  
      
    ) dbt_internal_test