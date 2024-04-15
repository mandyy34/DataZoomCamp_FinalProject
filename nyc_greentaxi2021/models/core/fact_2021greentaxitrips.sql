{{
    config(
        materialized='table'
    )
}}

with taxi_data as (
    select * from {{ ref('stg_2021_greentaxi') }} where pickup_date between '2021-01-01' and '2021-07-31'
),

taxi_zone as (
    select * from {{ ref('stg_taxi_zone') }}
)

select taxi_data.tripid, 
    taxi_data.vendorid, 
    taxi_data.ratecodeid,
    taxi_data.ratecodeid_description,
    taxi_data.pickup_locationid, 
    pickup_zone.borough as pickup_borough, 
    pickup_zone.zone_name as pickup_zone, 
    taxi_data.dropoff_locationid,
    dropoff_zone.borough as dropoff_borough, 
    dropoff_zone.zone_name as dropoff_zone,  
    taxi_data.pickup_datetime, 
    taxi_data.dropoff_datetime,
    taxi_data.pickup_date, 
    taxi_data.dropoff_date,
    taxi_data.store_and_fwd_flag, 
    taxi_data.passenger_count, 
    taxi_data.trip_distance, 
    taxi_data.trip_type,
    taxi_data.trip_type_description,
    taxi_data.fare_amount, 
    taxi_data.extra, 
    taxi_data.mta_tax, 
    taxi_data.tip_amount, 
    taxi_data.tolls_amount, 
    taxi_data.ehail_fee, 
    taxi_data.improvement_surcharge, 
    taxi_data.total_amount, 
    taxi_data.payment_type, 
    taxi_data.payment_type_description
    from taxi_data
    inner join taxi_zone as pickup_zone
    on taxi_data.pickup_locationid = pickup_zone.zone_id
    inner join taxi_zone as dropoff_zone
    on taxi_data.dropoff_locationid = dropoff_zone.zone_id

