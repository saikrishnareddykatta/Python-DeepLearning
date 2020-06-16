import numpy as np
import random
# creating a random vector of float elements
x = np.random.uniform(1, 20, 20)
print(x)
print("-------")
# reshaping the vector into a matrix
y = x.reshape(4, 5)
print(y)
print("--------")
# finding the maximum element in each row and reshaping into a column
k = np.max(y, axis=1).reshape(-1,1)
print(k)
print("---------")
# replacing the maximum element in each row with 0
z = np.where(y == np.max(y, axis=1).reshape(-1,1), 0, y)
print(z)
