"""
delete -> delete elements from an array (return new element array, old array will not change)

np.delete(array, index, axis=None)
flatten array
"""
import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print(arr)
new_arr = np.delete(arr, 0) #remove index 0 element of arr 
print(new_arr)