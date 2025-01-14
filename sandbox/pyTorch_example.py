import torch
import numpy as np

# Creating a tensor from raw data
data = [[1, 2], [3, 4]]
x_data = torch.tensor(data)
print(x_data)

# Creating a tensor from a numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(f"{x_np} \n")

# Create a random tensor basing its values on x_data from earlier
x_rand = torch.rand_like(x_data, dtype=torch.float)
print(f"Random Tensor: \n {x_rand} \n")

# Shape controls the dimensions of the tensor
shape = (2, 4)  # Shape must be a tuple
ones_tensor = torch.ones(shape)
print(f"Ones Shaped Tensor: \n {ones_tensor}")
print(f"Datatype of tensor: {ones_tensor.dtype}")
print(f"Device tensor is stored on: {ones_tensor.device} \n")

# Use Linear Algebra operations on the tensor
# Does not work on cuda
y1 = x_data.matmul(x_data)
print(y1)

y2 = x_data @ x_data
print(y2)

y3 = x_data.mul(x_data)
print(y3)

# Move tensors to the GPU for faster processing
data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
tensor = torch.tensor(data1)
if torch.cuda.is_available():
    tensor = tensor.to("cuda")

print(f"First row: {tensor[0]}")
print(f"First column: {tensor[:, 0]}")
print(f"Last column: {tensor[..., -1]}")

t1 = torch.cat([tensor, tensor, tensor], dim=1)
print(t1)
