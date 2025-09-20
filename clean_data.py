# Import pandas library
import pandas as pd

# Basic function that cleans data
def clean_data(df):
    """
    This is a basic function, that takes a dataframe as argument and perform some cleaning functions.
    """

    # Drop duplicate rows
    df = df.drop_duplicates()

    # Strip whitespace from column names and standardise column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    return df 