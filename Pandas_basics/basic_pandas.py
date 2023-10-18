import pandas as pd

# Simple Data Selection Function
def selectData(data: pd.DataFrame):
    ''' This function takes a dataframe as an argument 
    and returns the selected student's name and age '''
    return data[data.student_id == 101][['name', 'age']]

# Return the Size of a Dataframe
def getDataFrameSize(df: pd.DataFrame):
    ''' This function takes a dataframe as an argument 
    and returns the size of the dataframe as a list '''
    return list(df.shape)

# Return the 1st Three Rows
def selectFirstThreeRows(df: pd.DataFrame):
    ''' This function takes a dataframe as an argument 
    and returns the first three rows of the dataframe '''
    return df.head(3)

# Create a new bonus column
def createBonusCol(df: pd.DataFrame):
    ''' This function takes a dataframe as an argument, 
    creates a new column named 'bonus', which is a 
    doubling of the 'salary' column. It then returns 
    the updated dataframe '''
    df['bonus'] = df.salary * 2
    return df

# Drop Duplicate Rows from 'email' Column
def dropDupEmails(df: pd.DataFrame):
    '''This function takes a dataframe as an argument
    and drops duplicate rows based on emails 
    (while keeping the first instance). Then returns
    the updated dataframe'''
    df.drop_duplicates(subset='email', keep='first', inplace=True)
    return df

# Drop Rows with Missing Values
def dropMissingData(df: pd.DataFrame):
    '''This function takes a dataframe as an argument
    and drops rows with missing values. Then returns
    the updated dataframe'''
    return df.dropna()

# Double 'salary' Column
def doubleSalary(df: pd.DataFrame):
    '''This function takes a dataframe as an argument,
    doubles the 'salary' column, and then returns
    the updated dataframe'''
    df['salary'] = df.salary * 2
    return df

# Rename Columns
def renameCols(df: pd.DataFrame):
    '''This function takes a dataframe as an argument,
    renames the columns, and returns the updated dataframe'''
    return df.rename(columns = {'id':'student_id', 'first':'first_name',
                                'last':'last_name', 'age':'age_in_years'})

# Change Data Type of 'grade'
def changeDataType(df: pd.DataFrame):
    '''This function takes a dataframe as an argument,
    changes the 'grade' data type to int, and returns 
    the updated dataframe'''
    return df.astype({'grade': int})

# Replace Missing Values
def replaceMissingVals(df: pd.DataFrame):
    df.quantity.fillna(0, inplace=True)
    return df