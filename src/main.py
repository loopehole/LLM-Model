from src.model.llm_model import LLMModel
from src.utils import save_model, load_model
from src.data_cleaning import clean_data
import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    return clean_data(data)

def main():
    data = load_data('data/dataset.csv')
    # Assume data split into features and targets
    # data processing logic
    features = data.iloc[:, :-1]
    targets = data.iloc[:, -1]

    train_loader = torch.utils.data.DataLoader(
        list(zip(torch.tensor(features.values, dtype=torch.float32),
                 torch.tensor(targets.values, dtype=torch.float32))),
        batch_size=32, shuffle=True
    )

    model = LLMModel()
    model.train_model(train_loader, epochs=10)

    save_model(model, 'models/llm_model.pth')

if __name__ == "__main__":
    main()
