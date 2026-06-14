import numpy as np

#设置参数

mu = 0 #均值
sigma = 1 #标准差
x = 1.5 #待计算的点

pdf_value = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu) ** 2) / (2 * sigma ** 2))

print(f"标准正态分布在 x={x} 处的概率密度值为: {pdf_value:.6f}")

