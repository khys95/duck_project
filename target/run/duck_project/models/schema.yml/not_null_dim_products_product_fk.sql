
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select product_fk
from "analytics"."main"."dim_products"
where product_fk is null



  
  
      
    ) dbt_internal_test