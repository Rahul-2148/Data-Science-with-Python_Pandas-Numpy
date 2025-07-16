#astype -> convert data type of array (like int64 to float64 or convert the text to number)

import numpy as np

arr = np.array([1.2, 2.5, 3.8])
int_arr = arr.astype(int) #type will kuch bhi int, float or string ho skta h

print(arr.dtype)
print(int_arr)
print(int_arr.dtype)