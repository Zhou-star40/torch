import torch

str = "runoob"
print(len(str))

l = [1, 2, 3, 4, 5]
print(len(l))#列表元素个数

x = torch.arange(20).reshape(4,5)
#只返回该数据结构最外层（即第0维度）的长度
print(len(x))
print(x)

