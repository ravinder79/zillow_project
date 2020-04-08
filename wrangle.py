
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
    customers = get_data_from_sql()
    #customers = pd.read_sql("SELECT customer_id, monthly_charges, tenure, total_charges FROM customers WHERE contract_type_id = 3", env.get_db_url('telco_churn'))
    customers['total_charges'] = customers['total_charges'].str.strip()
    customers = customers.replace(r'^\s*$', np.nan, regex=True)
    customers = customers.dropna()
    customers['total_charges'] = customers['total_charges'].astype(float)
    return customers
    

#print(customers.sort_values(by='total_charges'))
#print(f' Shape = {customers.shape}')
#print(f'Describe = {customers.describe()}')