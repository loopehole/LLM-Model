import pandas as pd

def clean_data(df):
    """Clean the DataFrame by dropping missing values and duplicates."""
    df = df.dropna()  # Drop missing values
    df = df.drop_duplicates()  # Remove duplicates
    return df
