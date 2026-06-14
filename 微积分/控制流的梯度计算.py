import torch

def f(a):
    b = a * 2
    #b 会一直在 while 循环里翻倍，直到 b 的“大小”达到或超过 1000，然后才进入 if 判断。
    while b.norm() < 1000:
        b = b * 2
    if b.sum() > 0:
        c = b
    else:
        c = 100 * b
    return c
#函数里面的 return c，就是把 c 送出去；外面的 d = f(a)，就是用 d 接住这个 c
a = torch.tensor(400.0,requires_grad=True)
#存在某个标量k，使f(a)=k*a
#k 的数值就是这一次函数最终把 a 放大了多少倍
d = f(a)

d.backward()

print(a.grad == d / a)

print(a.grad)