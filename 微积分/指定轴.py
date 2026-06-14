import matplotlib.pyplot as plt
#创建一个空画布没有子图figure不自动带坐标系
fig = plt.figure()
#在画布上手动添加一个坐标系
#add_axes([左, 下, 宽, 高])
ax = fig.add_axes([0,0,1,1])
#.spines 坐标系的四条边框（脊线），是一个字典
ax.spines['bottom'].set_color('blue')
ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)
#将顶部和右侧设置为none
ax.spines['right'].set_color(None)
ax.spines['top'].set_color(None)
ax.plot([1,2,3,4,5])
plt.show()