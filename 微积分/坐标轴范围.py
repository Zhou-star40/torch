import matplotlib.pyplot as plt
import numpy as np
fig, axes = plt.subplots(1,1, figsize=(10,4))
x = np.arange(10)
axes.plot(x, np.exp(x),'r')
axes.set_title('exp')
axes.set_xlabel('x-axis')
axes.set_ylabel('y-axis')
#设置x轴的范围
axes.set_xlim(0,100)
#设置y轴的范围
axes.set_ylim(0,5000)
plt.show()
