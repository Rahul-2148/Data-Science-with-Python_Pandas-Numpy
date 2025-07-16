"""
reshape(rows, columns) specify new shape
if dimensions match
reshaping doesn't create a copy, it returns a view means original array will be changed
"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
reshaped_Arr = arr.reshape(2, 3)  #2 rows and 3 columns

print(reshaped_Arr)