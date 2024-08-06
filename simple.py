# ensure that the data is loaded correctly
import pandas as pd

file_path = 'data/dataset.csv'

try:
    data = pd.read_csv(file_path)
    print(data)
except Exception as e:
    print(f"Error loading data: {e}")
