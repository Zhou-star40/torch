import math
import time
import numpy as np
import torch
from d2l import torch as d2l

n = 10000
a = torch.ones([n])
b = torch.ones([n])

#定义一个计时器工具
#我要定义一个新的东西，叫Timer，是自定义类
## Timer 是一个自定义计时器类，可以理解成“秒表模板”
class Timer:
    #__init__ 对象刚出生时自动执行的准备工作
    def __init__(self):
        #需要一个空列表，用来记录每次时间
        self.times = []
        #马上开始计时
        self.start ()

    def start(self):
        #启动计时器
        #记录当前时间：调用 time 模块中的 time() 函数，得到当前时间戳
        #self.tik 用来保存本次计时开始的时间
        self.tik = time.time()
    
    #给Timer类定义一个方法，名字叫stop
    def stop(self):
        #停止计时器并将时间记录在其中
        #列表.append(新元素)
        self.times.append(time.time() - self.tik)
        return self.times[-1]
    
    def avg(self):
        return sum(self.times) / len(self.times)
    
    def sum(self):
        return sum(self.times)
    
    def cumsum(self):
        return np.array(self.times).cumsum().tolist()
    
c = torch.zeros(n)
timer = Timer()
for i in range(n):
    c[i] = a[i] + b[i]
print(f'{timer.stop(): .5f} sec')