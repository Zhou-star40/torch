import torch
import matplotlib.pyplot as plt

#生成训练数据

x  = torch.randn(100).reshape(-1, 1)

print(x)

y = 2 * x + 1 + torch.randn(100, 1) * 1.0

#初始化模型参数

w = torch.tensor([[0.0]], requires_grad=True)
b = torch.tensor([[0.0]], requires_grad=True)

learning_rate = 0.01

epochs = 100

loss_history = []

for epoch in range(epochs):

    # 预测值：ŷ = xw + b

    y_hat = x @ w + b

    # MSE 损失：预测值和真实值的平方误差平均

    loss = ((y_hat - y) ** 2).mean()

    # 反向传播：自动计算 loss 对 w 和 b 的梯度

    loss.backward()

    # 不让 PyTorch 记录下面的参数更新过程

    with torch.no_grad():

        # 梯度下降更新参数

        w -= learning_rate * w.grad

        b -= learning_rate * b.grad

        # 清空梯度，避免下一轮梯度累加

        w.grad.zero_()

        b.grad.zero_()

    # 保存当前 loss

    loss_history.append(loss.item())

    # 每 10 次打印一次结果

    if epoch % 10 == 0:

        print(f"第 {epoch} 次训练: loss={loss.item():.4f}, w={w.item():.4f}, b={b.item():.4f}")

# =========================

# 5. 训练结束后查看结果

# =========================

print("训练完成")

print("学到的 w:", w.item())

print("学到的 b:", b.item())

# =========================

# 6. 画出数据点和拟合直线

# =========================

plt.scatter(x.detach().numpy(), y.detach().numpy(), label="真实数据")

plt.plot(x.detach().numpy(), y_hat.detach().numpy(), label="模型预测直线")

plt.xlabel("x")

plt.ylabel("y")

plt.legend()

plt.grid()

plt.show()

plt.plot(loss_history)

plt.xlabel("训练次数 epoch")

plt.ylabel("损失 loss")

plt.title("Loss 下降曲线")

plt.grid()

plt.show()