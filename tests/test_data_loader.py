import pytest
from data.data_loader import load_data

def test_load_data():
    # Ensure this path exists or adjust the test as needed
    data = load_data('data/dataset.csv')
    assert data is not None
