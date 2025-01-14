import torch
import numpy as np
import matplotlib.pyplot as plt

data = [[1, 2], [3, 4]]
tensor = torch.tensor(data)
rand_tensor = torch.rand_like(tensor, dtype=torch.float)

labels_map = {
    0: 'Image 1',
    1: 'Image 2',
    2: 'Image Fun',
}
figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 1
for i in range(1, cols * rows + 1):
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[i - 1])

    match i:
        case 1:
            plt.plot([0, 0], [i, i*2])
        case 2:
            plt.plot(tensor.numpy())
        case 3:
            plt.plot(rand_tensor.numpy())
        case _:
            print('Invalid plot index')

plt.show()
