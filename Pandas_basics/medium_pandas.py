import pandas as pd

# Return Big Countries
def bigCountries(df):
    '''This function takes a dataframe as an argument,
    filters the dataframe to rows with 'area' greater than or equal to 3,000,000
    AND 'population' greater than or equal to 25,000,000, and returns the 'name',
    'population', and 'area' fields of the filtered dataframe'''
    return df[(df.area >= 3000000) | (df.population >= 25000000)][['name', 'population', 'area']]

# Return Products that are Low-Fat and Recyclable
def findProducts(df):
    '''This function takes a dataframe as an argument,
    filters the dataframe to rows with 'low_fats' equal to 'Y'
    AND 'recyclable' equal to 'Y', and returns the 'product_id' field of 
    the filtered dataframe'''
    return df[(df.low_fats == 'Y') & (df.recyclable == 'Y')][['product_id']]

# Return Customers who have not ordered
def findCustomers(customers, orders):
    return customers[~customers.id.isin(orders.customerId)][['name']].rename(columns={'name': 'Customers'})