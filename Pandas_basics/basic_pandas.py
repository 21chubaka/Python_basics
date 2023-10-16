import pandas as pd

# Simple Data Selection Function
def selectData(data: pd.DataFrame) -> pd.DataFrame:
    return data[data.student_id == 101][['name', 'age']]