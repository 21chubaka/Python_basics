import pandas as pd

# Return Big Countries
def bigCountries(df):
    return df[(df.area >= 3000000) | (df.population >= 25000000)][['name', 'population', 'area']]