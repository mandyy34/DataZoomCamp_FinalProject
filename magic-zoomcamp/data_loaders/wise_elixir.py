import pyarrow as pa
import pyarrow.parquet as pq
import os
import pandas as pd

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/secrets.json"

bucket_name = "magezoomcamp_finalprj"
project_id = 'finalprojectdataezoomcamp'

table_name = "2021_greentaxi"

root_path = f'{bucket_name}/{table_name}'


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    
    gcs = pa.fs.GcsFileSystem()

     # Define PyArrow schema
    arrow_schema = pa.schema([
        ('VendorID', pa.string()),
        ('lpep_pickup_datetime', pa.timestamp('ns')),
        ('lpep_dropoff_datetime', pa.timestamp('ns')),
        ('store_and_fwd_flag', pa.string()),
        ('RatecodeID', pa.int64()),
        ('PULocationID', pa.int64()),
        ('DOLocationID', pa.int64()),
        ('passenger_count', pa.int64()),
        ('trip_distance', pa.float64()),
        ('fare_amount', pa.float64()),
        ('extra', pa.float64()),
        ('mta_tax', pa.float64()),
        ('tip_amount', pa.float64()),
        ('tolls_amount', pa.float64()),
        ('ehail_fee', pa.float64()),
        ('improvement_surcharge', pa.float64()),
        ('total_amount', pa.float64()),
        ('payment_type', pa.int64()),
        ('trip_type', pa.int64()),
        ('congestion_surcharge', pa.float64()),
        ('lpep_dropoff_date', pa.date32()),
        ('lpep_pickup_date', pa.date32())
    ])

    table = pq.read_table(
        source=root_path,
        filesystem=gcs,
        schema=arrow_schema
    )

    df = table.to_pandas()
    
    
    return df


