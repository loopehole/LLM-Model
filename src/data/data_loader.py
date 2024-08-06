import pandas as pd
import os

def load_data(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"File is empty: {file_path}")
    
    data = pd.read_csv(file_path)
    
    if data.empty:
        raise ValueError("No columns to parse from file")
    
    return data
