import torch
import torch.nn as nn
import torch.optim as optim

class LLMModel(nn.Module):
    def __init__(self):
        super(LLMModel, self).__init__()
        self.fc1 = nn.Linear(10, 5)  # Example layers
        self.fc2 = nn.Linear(5, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

    def train_model(self, train_loader, epochs=10):
        criterion = nn.MSELoss()
        optimizer = optim.SGD(self.parameters(), lr=0.01)
        self.train()
        for epoch in range(epochs):
            for inputs, targets in train_loader:
                optimizer.zero_grad()
                outputs = self(inputs)
                loss = criterion(outputs, targets)
                loss.backward()
                optimizer.step()
            print(f"Epoch {epoch+1}/{epochs}, Loss: {loss.item()}")
