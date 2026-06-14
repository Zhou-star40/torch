import torch

x = torch.tensor([1.0,0.0,2.0])

x = x.to("mps")

x.requires_grad_(True)

v = torch.tensor([0.0,1.0,-1.0])

v = v.to("mps")

y = 5 * torch.dot(x,x) + 3 * torch.dot(x,v)

y = y.to("mps")
y.backward()

print(torch.backends.mps.is_available())
print(x.device)
print(x.grad)