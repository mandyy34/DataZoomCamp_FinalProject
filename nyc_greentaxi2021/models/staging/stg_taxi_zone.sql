{{ 
  config(
    materialized='table',
    
)}}

with taxi_zone as (
    select * from {{ source('staging','taxi_zone') }} WHERE zone_id IS NOT NULL AND zone_id != ''
  AND zone_name IS NOT NULL AND zone_name != ''
)

select 
cast(zone_id as integer) as zone_id,
zone_name,
borough,
zone_geom
 from taxi_zone