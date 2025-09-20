# Import pandas library
import pandas as pd

# This script contains two data loading functions

# Function one: Load data to CSV file
def load_to_csv(df, filename ="output.csv"):
    """
    This function takes the cleaned and transformed dataframe and stores it as a csv file
    """
    df.to_csv(filename, index = False)
    print(f"Data saved to {filename}")


# Function two: Load data to JSON file
def load_to_json(df, filename ="output.json"):
    """
    This function takes the cleaned and transformed dataframe and stores it as a json file
    """
    df.to_json(filename, orient = "records", lines = True)
    print(f"Data saved to {filename}")