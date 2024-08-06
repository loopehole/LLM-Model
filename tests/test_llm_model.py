import pytest
from model.llm_model import LLMModel

def test_model_initialization():
    config = {
        'tokenizer': 'bert-base-uncased',
        'model': 'bert-base-uncased'
    }
    model = LLMModel(config)
    assert model.model is not None
