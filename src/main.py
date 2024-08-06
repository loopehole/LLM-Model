from model.llm_model import LLMModel
from data.data_loader import load_data
from config.settings import CONFIG

def main():
    # Load and preprocess data
    data = load_data(CONFIG['data_path'])
    
    # Initialize and run LLM model
    model = LLMModel(CONFIG['model_params'])
    model.train(data)

if __name__ == "__main__":
    main()
