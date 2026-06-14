import torch

u = torch.tensor([3.0, -4.0])

print(torch.norm(u, p=2))#L2范数 求取向量的长度

print(torch.abs(u).sum())#L1范数 求取向量的绝对值之和

print(torch.norm(torch.ones((4, 9)), p='fro'))#Frobenius范数 求取矩阵的长度

