import pandas as pd

# Simple Data Selection Function
def selectData(data: pd.DataFrame) -> pd.DataFrame:
    ''' This function takes a dataframe argument and returns
        the selected student's name and age '''
    return data[data.student_id == 101][['name', 'age']]

# Return the Size of a Dataframe
def getDataFrameSize(df: pd.DataFrame) -> List[int]:
    return list(df.shape)