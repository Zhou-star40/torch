import numpy as np
import matplotlib.pyplot as plt
#fig画布 axes子图区域
#创建 1 行 3 列的子图，画布大小 12×4 英寸
fig, axes = plt.subplots(1,3, figsize=(12, 4))
x = np.arange(1, 11)
#子图0，x = x^3 线条颜色green 线宽 2 
axes[0].plot(x, x ** 3, 'g', lw=2)
#开启网格
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
#设置网格的颜色，线型，线宽
axes[1].grid(color='b', ls = '-.', lw = 2)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
#紧凑布局 自动调整子图间距，防止标题和坐标轴重叠
fig.tight_layout()
#显示渲染好的图
plt.show()

