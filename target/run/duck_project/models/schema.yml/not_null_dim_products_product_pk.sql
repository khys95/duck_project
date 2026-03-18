
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select product_pk
from "analytics"."main"."dim_products"
where product_pk is null



  
  
      
    ) dbt_internal_test