# ndim -> Returns the number of dimensions of the array
import numpy as np

arr_1d = np.array([1,2,3])
arr_2d = np.array([[1,2,3], [4,5,6]])
arr_3d = np.array([[[1,2], [3,4], [5,6], [7,8]]])

print(arr_1d.ndim)
print(arr_2d.ndim)
print(arr_3d.ndim)

# output
# 1 (shows 1 dimension array)
# 2 (shows 2 dimension array)
# 3 (shows 3 dimension array)