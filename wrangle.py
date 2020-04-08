
import pandas as pd
import numpy as np
import env

def get_db_url(database):
    from env import host, user, password
    url = f'mysql+pymysql://{user}:{password}@{host}/{database}'
    return url

def get_data_from_sql():
    query = """
    SELECT bathroomcnt AS bathrooms, bedroomcnt AS bedrooms, `calculatedfinishedsquarefeet` AS square_feet, fips, `lotsizesquarefeet` AS lot_size, poolcnt AS pool, `regionidzip` AS zip_code, yearbuilt AS year_built, `taxvaluedollarcnt` AS assessed_value, `taxamount` AS tax_value, transactiondate AS transaction_date FROM properties_2017
    JOIN predictions_2017 USING (parcelid)
    WHERE transactiondate >= '2017-05-01' AND transactiondate <= '2017-06-30'
    AND propertylandusetypeid = 261 AND bedroomcnt > 0 AND bathroomcnt> 0
    """
    df = pd.read_sql(query, get_db_url('zillow'))
    return df

def wrangle_zillow():
    """
    Queries the zillow database
    Returns a clean df with four columns:
    customer_id(object), monthly_charges(float), tenure(int), total_charges(float)
    """
    df = get_data_from_sql()
    df = df.dropna(subset=['lot_size', 'year_built', 'tax_value', 'zip_code'])
    df.fillna(0, inplace = True)
    df['fips'] =df.fips.astype(int)
    df['zip_code'] =df.zip_code.astype(int)
    df['year_built'] =df.year_built.astype(int)
    df['lot_size'] =df.lot_size.astype(int)
    df['pool'] =df.pool.astype(int)
    return df
    

#print(customers.sort_values(by='total_charges'))
#print(f' Shape = {customers.shape}')
#print(f'Describe = {customers.describe()}')