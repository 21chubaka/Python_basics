import pandas as pd

# Return Big Countries
def bigCountries(df):
    '''
    This function takes a dataframe as an argument,
    filters the dataframe to rows with 'area' greater than or equal to 3,000,000
    AND 'population' greater than or equal to 25,000,000, and returns the 'name',
    'population', and 'area' fields of the filtered dataframe
    '''
    return df[(df.area >= 3000000) | (df.population >= 25000000)][['name', 'population', 'area']]

# Return Products that are Low-Fat and Recyclable
def findProducts(df):
    '''
    This function takes a dataframe as an argument,
    filters the dataframe to rows with 'low_fats' equal to 'Y'
    AND 'recyclable' equal to 'Y', and returns the 'product_id' field of 
    the filtered dataframe
    '''
    return df[(df.low_fats == 'Y') & (df.recyclable == 'Y')][['product_id']]

# Return Customers who have not ordered
def findCustomers(customers, orders):
    '''
    This function takes two dataframes as an argument and 
    returns a dataframe of the name of customers who have
    never ordered anything
    '''
    return customers[~customers.id.isin(orders.customerId)][['name']].rename(columns={'name': 'Customers'})

# Return Authors that Viewed their own Articles
def ownArticleViews(views):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe of the id of the Authors that viewed
    their own Article
    '''
    return views[views.author_id == views.viewer_id][['author_id']
            ].drop_duplicates().rename(columns={
                'author_id': 'id'}).sort_values(by='id')

# Return Invalid Tweets by length
def invalidTweets(tweets):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe of the 'tweet_id's of invalid tweets,
    which are tweets with a character length greater than 15
    '''
    return tweets[tweets.content.str.len() > 15][['tweet_id']]

# Calculate Bonus Column for Employees
def calcSpecialBonus(employees):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe with a new 'bonus' column. The bonus
    is 100% of the employee's salary if the employee's id is 
    an odd number AND the employee's name does not start with
    the letter M
    '''
    employees['bonus'] = employees.apply(lambda x: x['salary'] if int(x['employee_id']) % 2 != 0 and
                                            not x['name'].startswith('M') else 0, axis=1)
    result = employees[['employee_id', 'bonus']].sort_values(by='employee_id', ascending=True)
    return result

# Capitalize Names
def capNames(users):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe with the names capitalized and
    sorted by user id
    '''
    users['name'] = users.name.str.capitalize()
    result = users.sort_values(by='user_id', ascending=True)
    return result