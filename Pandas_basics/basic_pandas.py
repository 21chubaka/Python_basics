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