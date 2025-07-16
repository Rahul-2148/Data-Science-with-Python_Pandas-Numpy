"""
concatenate -> merge two or more arrays at a specific axis or position 

np.concatenate((array1, array2), axis=0)

axis = 0 -> vertically stacking (row-wise)
axis = 1 -> horizontally stacking (column-wise)
"""

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

new_arr = np.concatenate((arr1, arr2))
print(new_arr)