import torch

x = torch.tensor([2.0], requires_grad=True)
#首先计算y的数值 y = 5 * 2 ** 2 = 20
y = 5 * x ** 2
#y和u的数值一样，detach后，不再追踪y是怎么由x计算出来的
u = y.detach()
#求导时，将u 看成常数
z = u * x ** 2 
#反向传播，计算z对x对梯度
z.sum().backward()

print(x.grad)

