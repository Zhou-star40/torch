import torch

x = torch.arange(12)

print(x.reshape(3,4))

print(x.reshape(2,2,3))

y = x.clone()

print(y)