"""
np.insert(array, index, values, axis=None)
array - original array
index - index or position no. at which values will be inserted
values - values to be inserted
axis - axis along which values will be inserted
axis = 0, row-wise
axis = 1, column-wise
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
new_arr = np.insert(arr, 2, 100, axis=0) #inserting 100 at position 2 at row wise
print(new_arr)