import matplotlib.pyplot as plt

x = [1,2,3]

y1 = [1,4,9]
y2 = [1,2,3]

plt.plot(x, y1, label='square')
plt.plot(x, y2, label='line')
#加上图例
plt.legend()

plt.show()