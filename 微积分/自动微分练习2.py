import torch

x = torch.tensor([0,-1,2,4], dtype = torch.float32)

print("x的数值",x)

x.requires_grad_(True)
x.grad

y = torch.dot(x,x) - 2 * x.sum()

y.backward()

print("梯度：",x.grad)

