import pytest
import torch
from src.model.llm_model import LLMModel
from src.utils import save_model, load_model
from src.data_cleaning import clean_data
import pandas as pd

def test_model_training():
    model = LLMModel()
    dummy_data = pd.DataFrame({
        'feature1': [1.0, 2.0],
        'feature2': [3.0, 4.0],
        'target': [1.0, 0.0]
    })
    cleaned_data = clean_data(dummy_data)
    features = cleaned_data[['feature1', 'feature2']]
    targets = cleaned_data['target']
    train_loader = torch.utils.data.DataLoader(
        list(zip(torch.tensor(features.values, dtype=torch.float32),
                 torch.tensor(targets.values, dtype=torch.float32))),
        batch_size=1, shuffle=True
    )
    model.train_model(train_loader, epochs=1)

def test_save_load_model():
    model = LLMModel()
    save_model(model, 'models/test_model.pth')
    new_model = LLMModel()
    load_model(new_model, 'models/test_model.pth')
    assert model.state_dict() == new_model.state_dict()
