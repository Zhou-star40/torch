import torch
import random

features = torch.tensor([
    [1.0, 10.0],
    [2.0, 20.0],
    [3.0, 30.0],
    [4.0, 40.0],
    [5.0, 50.0],
    [6.0, 60.0],
    [7.0, 70.0],
])

labels = torch.tensor([
    [100.0],
    [200.0],
    [300.0],
    [400.0],
    [500.0],
    [600.0],
    [700.0],
])

def my_data_iter(batch_size, features, labels):
    num_example = len(features)
    indices = list(range(num_example))
    #indices表示当前这一批具体要取哪些样本编号
    random.shuffle(indices)

    for i in range(0, num_example, batch_size):
        batch_indices = torch.tensor(
            indices[i: min(i + batch_size, num_example)]
        )

        yield features[batch_indices], labels[batch_indices]


batch_size = 3

for X, y in my_data_iter(batch_size, features, labels):
    print("X =", X)
    print("y =", y)
    print("------")