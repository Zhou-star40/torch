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
#2个权重
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

#我要造一个可以重复使用的小工具
#batch_size 表示每一批次有多少条样本
#features 特征矩阵
#labels 标签向量
#data_iter 是用来每次取出一小批数据，交给后面的训练过程
#也就是说他只负责“喂数据”，不负责“学习”
def data_iter(batch_size, features, labels):
    num_example = len(features) #len函数
    #生成样本的编号
    #如果num_example = 5 那么range = 0，1，2，3，4
    #list就是把这些编号编程列表
    indices = list(range(num_example))
    #打乱所有样本编号列表
    #shuffle的重点是：元素不变，只改变顺序
    random.shuffle(indices)
    #range(开始位置，结束位置，步长)
    #i = 当前批次的起始位置
    for i in range(0, num_example, batch_size):
        batch_size = torch.tensor(
            #从i的位置开始，取到i + batch_size为止
            #i 和 i+batch_size 是“位置范围” 切片返回的是这些位置上的“值”
            #有min是告诉你最多取到样本总数 num_examples
            indices[i: min(i + batch_size, num_example)])
#features和labels必须用同一组batch_indices，是为了保证每个样本的特征和他自己的标签一一对应
#用同一批编号，同时取出这一批样本的输入 X 和真实答案 y
# yield 感觉就是每次吐出一批数据，然后暂停，下一次循环再接着吐下一批    
        yield features[batch_size], labels[batch_size]

#一次拿一小批数据
#每次取出来10个样本，不是1000个
batch_size = 10 

for X, y in data_iter(batch_size, features, labels):
    print(X, '\n', y)
    #只看第一批数据，看完就跳出循环
    break

#torch.normal 从正态分布里面随机取数， 0 是均值， 0.01 是标准差 size=(2,1) 表示生成出来的w是2行1列
w = torch.normal(0, 0.01, size=(2,1), requires_grad=True)
b = torch.zeros(1, requires_grad=True)

def linreg(X, w, b):
    #定义模型
    return torch.matmul(X, w) + b

def squared_loss(y_hat, y):
    #均方损失
    #y_hat：模型预测值
    #y: 真实值
    return (y_hat - y.reshape(y_hat.shape)) ** 2 / 2

# 优化算法的任务，就是根据梯度更新参数，然损失变小




