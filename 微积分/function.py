#f(x)=x²+2x+1
import torch

from matplotlib_inline import backend_inline

import matplotlib.pyplot as plt #导入画图工具箱

y = torch.arange(10, dtype=torch.float32)

print(y.shape)

fig, axes = plt.subplots()

def f(x):
    return x ** 2 + 2 * x + 1

def set_axes(axes, legend):
    if legend:
        axes.legend(legend)
    axes.grid(True)

set_axes(axes,['f(x)'])

plt.show()