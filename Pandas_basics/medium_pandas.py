import pandas as pd
import numpy as np

# Return Big Countries
def bigCountries(df):
    '''
    This function takes a dataframe as an argument,
    filters the dataframe to rows with 'area' greater than or equal to 3,000,000
    AND 'population' greater than or equal to 25,000,000, and returns the 'name',
    'population', and 'area' fields of the filtered dataframe
    Args: DataFrame
    Returns: DataFrame
    '''
    return df[(df.area >= 3000000) | (df.population >= 25000000)][['name', 'population', 'area']]

# Return Products that are Low-Fat and Recyclable
def findProducts(df):
    '''
    This function takes a dataframe as an argument,
    filters the dataframe to rows with 'low_fats' equal to 'Y'
    AND 'recyclable' equal to 'Y', and returns the 'product_id' field of 
    the filtered dataframe
    Args: DataFrame
    Returns: DataFrame
    '''
    return df[(df.low_fats == 'Y') & (df.recyclable == 'Y')][['product_id']]

# Return Customers who have not ordered
def findCustomers(customers, orders):
    '''
    This function takes two dataframes as an argument and 
    returns a dataframe of the name of customers who have
    never ordered anything
    Args: Two DataFrames
    Returns: DataFrame
    '''
    return customers[~customers.id.isin(orders.customerId)][['name']].rename(columns={'name': 'Customers'})

# Return Authors that Viewed their own Articles
def ownArticleViews(views):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe of the id of the Authors that viewed
    their own Article
    Args: DataFrame
    Returns: DataFrame
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
    Args: DataFrame
    Returns: DataFrame
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
    Args: DataFrame
    Returns: DataFrame
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
    Args: DataFrame
    Returns: DataFrame
    '''
    users['name'] = users.name.str.capitalize()
    result = users.sort_values(by='user_id', ascending=True)
    return result

# Find Valid Emails
def validEmails(users):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe with the rows of users that have
    valid emails. 
    A valid e-mail has a prefix name and a domain where:
        - The prefix name is a string that may contain letters (upper or lower case), 
            digits, underscore '_', period '.', and/or dash '-'. 
        - The prefix name must start with a letter.
        - The domain is '@leetcode.com'.
    Args: DataFrame
    Returns: DataFrame
    '''
    return users[users.mail.str.match(r'^[a-zA-Z][a-zA-Z\d_.-]*@leetcode\.com')]

# Find Type 1 Diabetes Patients
def findPatients(patients):
    '''
    This function takes a dataframe as an argument and 
    returns a dataframe with the rows of patients who have
    Diabetes in their condition.
    Args: DataFrame
    Returns: DataFrame
    '''
    return patients[patients.conditions.str.contains(r'\bDIAB1')]

# Count Occurences of 'bear' and 'bull'
def countOccurr(files):
    '''
    This function takes a dataframe as an argument and 
    returns the number of occurences of 'bull' and 'bear'
    as a dataframe.
    Args: DataFrame
    Returns: DataFrame
    '''
    return pd.DataFrame({'word': ['bull', 'bear'], 
                         'count': [files.content.str.contains(' bull ').sum(), 
                                   files.content.str.contains(' bear ').sum()]})

# Return Nth Highest Salary
def nthHighestSalary(employee, N):
    '''
    This function takes a dataframe and int number as arguments and 
    returns the Nth highest salary using the int number as Nth. If there
    is no Nth highest salary it returns null.
    Args: DataFrame & Integer
    Returns: DataFrame
    '''
    df = employee.salary.drop_duplicates()
    if len(df) < N:
        return pd.DataFrame([np.NaN], columns=[f'getNthHighestSalary({N})'])
    else:
        result = sorted(df, reverse=True)[N-1]
        return pd.DataFrame([result], columns=[f'getNthHighestSalary({N})'])
    
# Return 2nd Highest Salary
def secondHighestSalary(employee):
    '''
    This function takes a dataframe as an argument and returns 
    the 2nd highest salary as a dataframe. If there is no 2nd 
    highest salary it returns null.
    Args: DataFrame
    Returns: DataFrame
    '''
    df = employee.salary.drop_duplicates()
    if len(df) < 2:
        return pd.DataFrame([np.NaN], columns=['SecondHighestSalary'])
    else:
        result = sorted(df, reverse=True)[1]
        return pd.DataFrame([result], columns=['SecondHighestSalary'])

# Join two DataFrames by Column
def employeeDepartmentJoin(employee, department):
    '''
    This function takes two dataframes as arguments, joins the
    two dataframes on the Department ID field, and returns the
    result of the join as a dataframe
    Args: Two DataFrames
    Returns: DataFrame
    '''
    department.rename(columns={'id': 'departmentId', 'name': 'Department'}, inplace=True)
    employee.rename(columns={'name': 'Employee', 'salary': 'Salary'}, inplace=True)
    df_join = pd.merge(employee, department, on='departmentId', how='inner')
    return df_join

# Return the Highest Salaried Employees from each Department
def departmentHighestSalary(employee, department):
    '''
    This function takes two dataframes as arguments, joins the
    two dataframes on the Department ID field, and returns the
    the Employee's name, department, and salary of the highest
    paid employee(s) from each department
    Args: Two DataFrames
    Returns: DataFrame
    '''
    # Rename columns
    department.rename(columns={'id': 'departmentId', 'name': 'Department'}, inplace=True)
    employee.rename(columns={'name': 'Employee', 'salary': 'Salary'}, inplace=True)

    # Join department and employee dataframes on Department ID
    df_join = pd.merge(employee, department, on='departmentId', how='inner')

    # Grab highest salaries of each department and filter dataframe
    max_sal = df_join.groupby('departmentId')['Salary'].transform('max')
    df_sal = df_join[df_join['Salary'] == max_sal]

    # Config columns for result
    result = df_sal[['Department', 'Employee', 'Salary']]
    return result

# Ranking Scores
def rankScores(scores):
    '''
    This function takes a dataframe as an argument, ranks the
    scores and returns a dataframe of the scores and rank ordered
    by the scores from highest to lowest
    Args: DataFrame
    Returns: DataFrame
    '''
    scores['rank'] = scores.score.rank(method='dense', ascending=False)
    result = scores[['score', 'rank']].sort_values(by='score', ascending=False)
    return result

# Drop Duplicate Emails
def deleteDupEmails(person):
    '''
    This function takes a dataframe as an argument
    and drops duplicate rows based on emails 
    (while keeping the first instance). Then returns
    the updated dataframe
    Args: DataFrame
    Returns: DataFrame
    '''
    person.sort_values(by='id',ascending=True,inplace=True)
    person.drop_duplicates(subset='email', keep='first', inplace=True)
    return person

# Reshape DataFrame using Melt
def rearrange_products_table(products):
    '''
    This function takes a dataframe as an argument,
    reshapes the dataframe using melt, and returns the updated dataframe
    Args: DataFrame
    Returns: DataFrame
    '''
    return products.melt(id_vars=['product_id'], var_name='store', value_name='price').dropna()

# Return the Number of Customers
def countRichCustomers(store):
    '''
    This function takes a dataframe as an argument 
    and returns the number of Customers where amount
    is greater than 500 as a dataframe
    Args: DataFrame
    Returns: DataFrame
    '''
    return pd.DataFrame(store[store.amount > 500][['customer_id']].nunique(), columns=['rich_count'])

# Return Immediate Food Delivery Percentage
def immedFoodDelivPercent(delivery):
    '''
    This function takes a dataframe as an argument 
    and returns the Percentage of Immediate Deliveries.
    Which is orders that have the same date the customer's
    preferred delivery date divided by total orders.
    Args: DataFrame
    Returns: DataFrame
    '''
    immed_count = delivery[delivery.order_date == delivery.customer_pref_delivery_date].shape[0]
    tot_orders = delivery.shape[0]
    immed_percent = (immed_count / tot_orders) * 100
    result = pd.DataFrame({'immediate_percentage': [round(immed_percent, 2)]})
    return result