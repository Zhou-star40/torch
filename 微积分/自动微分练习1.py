import torch

x = torch.arange(1.0,4.0)
print(x)

x.requires_grad_(True)
x.grad
y = 3 * torch.dot(x,x)
y.backward()
print(x.grad)

