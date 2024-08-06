import torch

def save_model(model, path):
    """Save the model's state dict to the specified path."""
    torch.save(model.state_dict(), path)

def load_model(model, path):
    """Load the model's state dict from the specified path."""
    model.load_state_dict(torch.load(path))
    model.eval()
