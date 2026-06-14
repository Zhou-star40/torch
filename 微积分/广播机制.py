import torch

x = torch.arange(5).reshape(5,1)

y = torch.arange(40,65).reshape(5,5)

print(f'x {x}')

print(f'y {y}')

print(f'x+y {x+y}')
