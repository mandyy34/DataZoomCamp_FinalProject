# DataZoomCamp_FinalProject

# 1 Set Up Pipeline 1 to load data into GCP bucket (Week1/Week2/Week5)
* Grab data into my GCP bucket - partitioned by date
* Use of Mage to set up pipeline load_2021q1_greentripdata_to_gcp
* Data Loader : grab data from https links (batch loading)
* Transformer: transform the data
* Data Exporter: export data to my gcp bucket and save by patitioned date
(Was planning to do Q1 data only but as the 2021 data are up to 202107 only, so i grab all of it)

<img src="/workspaces/DataZoomCamp_FinalProject/Assets/GCP_bucket.png">

# 2 Set Up Pipeline 2 to load GCP parquet file to BigQuery (Week3)
* Load my GCP bucket data into BQ
* Use of Mage to set up pipeline gcsbucket_to_bigquery
* Data Loader: grab data from the partitioned parquet
(Need to provide schema when re-ingest to panda data frame; otherwise it will be exported in wrong schema to BQ)
* Transformer: do some fixes on the naming
* Data Exporter: export the data to table finalprojectdataezoomcamp.nycdata.2021_green_taxi

<img src="/workspaces/DataZoomCamp_FinalProject/Assets/BQ.png">

# 3 Set up dbt project nyc_greentaxi2021 (Week4)
* Use dbt to further clean the data
* Partition and cluster the table by pickup_date and vendorid
* Join the taxi_zone table with the green taxi trip data as fact table to be used for visualization
* Set up test to check the data in the table for not null, uniqueness, accepted value, etc
* Make use of the macros to add the ratecodeid_description and trip_type_description

<img src="/workspaces/DataZoomCamp_FinalProject/Assets/patition_cluster.png">
<img src="/workspaces/DataZoomCamp_FinalProject/Assets/dbt lineage.png">


# 4 Create Report on Looker Studio
* Aim: Provide insights to new taxi drivers
* Obstacles: 2021 was still under covid so the data may not tell the full picture
* Insights: 
    - With the ease of the lockdown policy, there is a increasing trend in the trips from 202103-202107
    - Choosing mid of the week to work, i.e. Wed to Fri, tends to have more trips made
    - When waiting for trips, going to East Harlem North/South and Central Harlem/ North will have more chances to 
      make a trip as they are popular pickup zones.
    - When looking for higher tips, please go Lenox Hill West, Midtown North or Broad Channel. Trips picking up from these places tends to have higher tips percentage. Also, when the dispatching system offering dropoff to Cobble Hill/Greenwich Village South or West Village, get these trips at once as people going to these places tends to give higher percentage of tips.
    - Because of covid, the airport pickup/dropoff trips are not much. But if driver wants to make the airport deal, go JFK Airport or be near will be best. It ranked top for both pickup and dropoff.


<img src="/workspaces/DataZoomCamp_FinalProject/Assets/Screenshot 2024-04-15 004133.png">


https://lookerstudio.google.com/s/ldeqmYqTJ7s