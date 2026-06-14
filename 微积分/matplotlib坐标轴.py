import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1,1, figsize=(10,4))
x = np.arange(1,5)
axes.plot(x, np.exp(x), 'r')
axes.plot(x, x**2, 'g')
axes.set_title("Normal scale")
#设置x轴
axes.set_xlabel("x axis")
axes.set_ylabel("y axis")
#调整图像x轴标签与轴的距离
axes.xaxis.labelpad =10
plt.show()