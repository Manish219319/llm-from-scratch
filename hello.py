import torch
x = torch.randn(3, 3)
print("PyTorch", torch.__version__)
print(x @ x.T)