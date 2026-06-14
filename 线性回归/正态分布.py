import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib_inline import backend_inline

def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)

x = np.arange(-7, 7, 0.01)

#传入三个参数， 三个不同的均值和标准差
params1 = [(0, 1)]
params2 = [(0, 2)]
params3 = [(3, 1)]

for mu, sigma in params1:
    plt.plot(x, normal(x, mu, sigma),'black',ls = '-.',label=f'params 1, mean {mu}, std {sigma}')

for mu, sigma in params2:
    plt.plot(x, normal(x, mu, sigma),'g',label=f'params 2, mean {mu}, std {sigma}')

for mu, sigma in params3:
    plt.plot(x, normal(x, mu, sigma),'r', ls = '--', label = f'params 3 , mean {mu} , std {sigma}')

plt.grid(color='b', ls = '-.', lw = 0.25)
plt.xlabel('x')
plt.ylabel('p(x)')
plt.legend()
plt.show()