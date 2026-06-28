import pandas as pd

def open_data(df: str):
    return pd.read_csv(df)
    
def clean_data_1(df):
    return df.head(len(df) - 2)

def clean_data_2(df):
    return df.tail(len(df) - 6)

    
    
    