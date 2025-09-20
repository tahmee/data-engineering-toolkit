# Import pandas library
import pandas as pd

# This script contains two data loading functions

# Function one: Load data to csv file
def load_to_csv(df, filename ="output.csv"):
    """
    This function takes the cleaned and transformed dataframe and stores it as a csv file
    """
    df.to_csv(filename, index = False)
    print(f"Data saved to {filename}")