import torch

x = torch.arange(20, dtype = torch.float32).reshape(4,5)

print(x)

def f(y):
    return y == torch.tensor(20)

y = torch.arange(21)

print(f(y))