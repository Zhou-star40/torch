# import torch
# import random
# def data_iter(batch_size, features, labels):
#     num_example = len(features)
#     indices = list(range(num_example))
#     random.shuffle(indices)
#     for i in range(0, num_example, batch_size):
#         batch_size = torch.tensor(
#             indices[i: min(i + batch_size, num_example)])
#         yield features[batch_size], labels[batch_size]

# batch_size = 10 

# for X, y in data_iter(batch_size, features, labels):
#     print(X, '\n', y)
#     break