
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    product_fk as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_products"
where product_fk is not null
group by product_fk
having count(*) > 1



  
  
      
    ) dbt_internal_test