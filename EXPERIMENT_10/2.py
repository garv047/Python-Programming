#Q2

import numpy as np

arr = np.array([[1, 5, 3],
                [8, 2, 7],
                [4, 9, 6]])

print("Array:\n", arr)

print("Row sums:", np.sum(arr, axis=1))

print("Column sums:", np.sum(arr, axis=0))

flat = arr.flatten()
second_max = np.sort(flat)[-2]

print("Second maximum element:", second_max)
