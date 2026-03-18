
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    asin as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_products"
where asin is not null
group by asin
having count(*) > 1



  
  
      
    ) dbt_internal_test