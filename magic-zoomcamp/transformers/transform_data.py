if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer

def transform(data, *args, **kwargs):

    df =  data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]  
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    df['lpep_dropoff_date'] = df['lpep_dropoff_datetime'].dt.date
    return df


@test
def test_output(output,  *args):
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are riders with zero passengers'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are no trips with zero distances'



