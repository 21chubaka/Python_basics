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