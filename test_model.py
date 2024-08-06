import unittest
import pandas as pd
from src.data.data_loader import load_data
from src.model import YourModelClass  # Replace with your actual model class

class TestModel(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Load the model once for all tests
        cls.model = YourModelClass.load('path/to/your/model')  # Adjust as needed

    def test_prediction(self):
        # Sample input data
        sample_data = pd.DataFrame({
            'feature1': [value1],  # Replace with actual feature names and values
            'feature2': [value1]
        })

        # Predict using the model
        predictions = self.model.predict(sample_data)  # Adjust method as needed

        # Check if predictions are as expected (update expected value as needed)
        self.assertEqual(predictions[0], expected_value)

if __name__ == "__main__":
    unittest.main()
