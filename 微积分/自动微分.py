import torch
#只有浮点型张量才能计算梯度
x = torch.arange(4.0)
print(x)
#希望张量x可以参与求导，记录和x有关的计算过程
#requires_grad_需要梯度
#直接将原来的x改成“需要梯度” 状态
x.requires_grad_(True)
x.grad #默认值是None 

#点积需要两个向量
y = 2 * torch.dot(x,x)

#调用反向传播函数来自动计算y关于x每个分量的梯度

y.backward() #开始从y反向求导
x.grad#查看y对x的导数结果

print(x.grad)

print(x.grad == 4 * x) #验证梯度是否正确

x.grad.zero_() #清除x的梯度
y = x.sum()
y.backward()
print(x.grad)

x.grad.zero_()
#根据x计算出一个新的张量y
y = x * x
#把向量里的所有元素加起来，合成一个标量，backward() 最喜欢从一个单独的数开始反向求导
#以 y.sum() 这个标量作为起点，反向传播，计算它对 x 的梯度
y.sum().backward()
#最后把求出来的梯度结果存到 x.grad 里面
print(x.grad)


