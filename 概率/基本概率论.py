import torch
import numpy as np
#导入多项分布相关模块
#torch.distributions 是专门处理概率分布的模块
from torch.distributions import multinomial
#坐标轴刻度格式化工具
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
from d2l import torch as d2l

#创建一个公平的骰子 
fair_probs = torch.ones([6]) / 6

#fair_probs 公平概率
print(fair_probs)

#创建一个多项分布对象
#第一个参数表示总共抽样1次
#第二个参数表示每个类别/结果出现的概率
#sample表示从这个分布中抽样
#从 torch.distributions 这个概率分布模块里，调用 Multinomial 类。
multinomial.Multinomial(1,fair_probs).sample()

print(multinomial.Multinomial(1,fair_probs).sample())

counts = multinomial.Multinomial(1000,fair_probs).sample()
#得到相对频率
print(counts / 1000)

#表示从这个分布中采样500组，每组抽取10个样本
#counts是每一组的单独统计
#cumsum(dim = 0)是从上往下累加
counts = multinomial.Multinomial(10, fair_probs).sample((500,))
#从上往下累加数据 
#每一个面出现的次数
cum_counts = counts.cumsum(dim=0)

print(cum_counts)
#将每一行横向加起来
#每一面出现的次数/当前总投掷次数
#将次数变成概率，keepdim是将求和后的结果不要降维度
estimates = cum_counts / cum_counts.sum(dim=1, keepdims=True)

print(estimates)
#书中的做法
# d2l.set_figsize((6,4.5))

# for i in range(6):
#     d2l.plt.plot(estimates[:,i].numpy(),
#               label=f"P(die={i +1})")

# d2l.plt.axhline(y=1/6, color="black", linestyle="dashed")
# d2l.plt.gca().set_xlabel('Groups of experiments')
# d2l.plt.gca().set_ylabel('Estimated probability')

# d2l.plt.legend();
# plt.show()
#设置画布大小
fig, ax = plt.subplots(figsize=(6,4.5))

for i in range(6): 
    #matplotlib更习惯处理numpy数组，label和legend联动，显示图例
    ax.plot(estimates[:,i].numpy(), label=("P(die="+ str(i + 1) + ")"))

#设置一条虚线，y=1/6
ax.axhline(y=1/6,color= 'black',linestyle='dashed')
ax.set_xlabel('Groups of experiments')
ax.set_ylabel('Estimated probability')
#将y轴保留3位小数


ax.legend();
plt.show()

