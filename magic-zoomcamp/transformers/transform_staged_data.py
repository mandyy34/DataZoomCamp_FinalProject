if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    df = data
    df.columns = (df.columns
                    .str.replace(' ', '_')
                    .str.lower()
                    )



    return data
