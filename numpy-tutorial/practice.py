import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

print([1, 2, 3] in arr.tolist())
print([1, 5, 3] in arr.tolist())