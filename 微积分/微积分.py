import numpy as np #导入numpy库，并命名为np

from matplotlib_inline import backend_inline #导入matplotlib_inline库中的backend_inline模块
#导入显示和渲染图形的 backend_inline模块
from d2l import torch as d2l #导入d2l库中的torch模块，并命名为d2l

def f(x):
    return 3 * x**2 - 4 * x #定义一个函数f(x) = 3x^2 - 4x

print(f(2)) 

def numerical_lim(f, x, h):
    return (f(x + h) - f(x)) / h    #定义一个函数numerical_lim，计算函数f在点x处的数值极限，使用差商的形式

h = 0.1
for i in range(10):    #循环5次，每次将h乘以0.1，逐渐减小h的值
    print(f'h={h:.10f}, numerical limit={numerical_lim(f, 1, h):.10f}')
    h *= 0.1

def use_svg_display():  #@save
    backend_inline.set_matplotlib_formats('svg')#使用svg格式显示图片，是矢量图放大不会糊， backend_inline 这是一个模块对象 来自from matplotlib_inline import backend_inline
    #对象.功能 从backend_inline中调用set_matplotlib_formats，用来设置图片格式'svg'
    #matplotlib=数学绘图库
def set_figsize(figsize=(3.5, 2.5)): #@save #设置图片大小 figsize（width，height）
    use_svg_display()#指向函数不会运行
    d2l.plt.rcParams['figure.figsize'] = figsize #修改matplotlib绘图库全局图像大小
    #rcParams（全局配置字典） matplotlib的全局参数配置
#@save
#set_axes 设置坐标轴
#legend 将画出的线显示出来 
#封装
def set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend):
    axes.set_xlabel(xlabel) #对象.功能(参数)
    axes.set_ylabel(ylabel) #ylabel y轴+label标签=x轴名称
    axes.set_xlim(xlim) #x轴限制范围
    axes.set_ylim(ylim)
    axes.set_xscale(xscale) #x轴比例类型
    axes.set_yscale(yscale)
    #判断下面为假，不会输出图例legend = []
    if legend: #如果 legend 不是空的 就执行下面代码
        axes.legend(legend) 
    axes.grid() #打开图像中的网格 等价于axes.grid(true)
    #axes.grid(false)关闭图像中的网格
#@save
#def plot()统一画图 定义一个超级绘图函数
def plot(X, Y=None, xlabel=None, ylabel=None, xlim=None, ylim=None, legend=None, xscale='linear', yscale='linear',
         fmts=('-','b--','g-.','r:'), figsize=(5.5,4.5), axes=None):
    #fmts 格式 '-'表示普通实线 'm--'表示紫色虚线 'g-.'表示点划线 'r:'红色点线 figsize图像大小 axes=none没有指定坐标轴对象
    if legend is None: #is 表示是不是同一个对象
        legend = [] #防止报错
        # 如果用户没有传入 legend（图例）
        # 就创建一个空列表 []
        # 防止后面操作 legend 时出现错误
        # 同时统一 legend 的数据类型，方便后续判断和使用

    set_figsize(figsize) #放置图像大小 将figsize参数传入
    axes = axes if axes else d2l.plt.gca() #三元表达式 d2l.ply.gca 获取当前坐标轴
    #如果用户没传axes，程序就自动获取当前对象
    def has_one_axis(X): #判断是否是一维数据 hasattr检查对象有没有某个属性 x是不是一维 isinstance：x是不是list类型  hasettr：x里面是不是普通数字，而不是二维嵌套列表
        return (hasattr(X, "ndim")) and X.ndim == 1 or isinstance(X, list) and not hasattr(X[0], "__len__")
        #and 只有左右两边都是true，整体才是true  or是有一个是true整体就是true ‘not true’ = false
    if has_one_axis(X):
        X = [X] #包装成二维列表 一次循环处理一整条直线
    if Y is None:
        X, Y = [[]] * len(X), X  #同时赋值  将原来的 X 当成 Y 创建空的 X 占位 后续 matplotlib 自动生成 x 坐标
    elif has_one_axis(Y):
        Y = [Y] #包装成二维列表
    if len(X) != len(Y): #!= 不等于
        X = X * len(Y) #列表 * 数字 表示重复列表
        axes.cla() #清理坐标轴 alean axes
    for x, y, fmt in zip(X, Y, fmts): #zip 将x y fmts 按顺序打包 一次取一组
        if len(x):
            axes.plot(x, y, fmt)
        else:
            axes.plot(y, fmt)
    set_axes(axes, xlabel, ylabel, xlim, ylim, xscale, yscale, legend) #统一图像设置

x = np.arange(0, 3, 0.1)
plot(x, [f(x), 2 * x - 3], 'x', 'f(x)', legend=['f(x)', 'Tangent line (x=1)'])

d2l.plt.show()