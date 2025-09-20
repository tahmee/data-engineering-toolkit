# Import pandas as pd
import pandas as pd

# Basic data transformation function
def transform_data(df):
    """
    This is a basic data transformation function that takes in a dataframe as input and 
    returns a transformed dataframe
    """

    # Normalizing numeric columns
    num_cols = df.select_dtypes(include=["number"]).columns
    for col in num_cols:
        if df[col].max() != df[col].min():  
            df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    return df