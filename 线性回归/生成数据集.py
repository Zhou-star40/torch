import random
import matplotlib.pyplot as plt
import torch
from d2l import torch as d2l

#先定义函数，不代表马上生成数据
#定义一个函数，w 表示真实权重， b 表示真实偏置， num_examples 表示要生成多少个样本
def synthetic_data(w, b, num_examples):
    #生成输入特征X，从均值为0，标准差为1的正态分布中，随机生成X
    #每个样本的特征数量等于 len(w)
    X = torch.normal(0, 1, (num_examples, len(w)))
    #matmul 矩阵相乘
    y = torch.matmul(X, w) + b
    #给标签y加噪声， += 是说在原来的y上加噪声
    y += torch.normal(0, 0.01, y.shape)
    return X, y.reshape((-1, 1))


#先设置一个真实参数权重w和偏置b
true_w = torch.tensor([2, -3.4])
true_b = 4.2
#生成1000个样本
features, labels = synthetic_data(true_w, true_b, 1000)
# 函数内部返回的 X 会被外面的 features 接住
# 函数内部返回的 y 会被外面的 labels 接住
print('features:', features[0], '\nlabel:', labels[0])

#设置图像大小
# d2l.set_figsize()
# #scatter()用于绘制散点图
# d2l.plt.scatter(features[:, (1)].detach().numpy(), labels.detach().numpy(), 1);
# plt.show()

def data_iter(batch_size, features, labels):
    num_example = len(features)
    indices = list(range(num_example))
    random.shuffle(indices)
    for i in range(0, num_example, batch_size):
        batch_size = torch.tensor(
            indices[i: min(i + batch_size, num_example)])
        yield features[batch_size], labels[batch_size]

batch_size = 10 

for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    break

w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)