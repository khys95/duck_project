
    
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    

select
    ship_city as unique_field,
    count(*) as n_records

from "analytics"."main"."dim_locations"
where ship_city is not null
group by ship_city
having count(*) > 1



  
  
      
    ) dbt_internal_test