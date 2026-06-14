import numpy as np
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,1, figsize =(5,5))

x = np.arange(12)

axes.plot(x, x**2 + x*5, 'r', lw = 2 )

axes.grid(color='g', ls='-', lw = 0.5)

axes.set_title('f(x)')

plt.show()
