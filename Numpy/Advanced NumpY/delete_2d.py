'''
delete 2d array -> delete elements from 2d array (return new element array, old array will unchanged.)
'''

import numpy as np

arr_2d = np.array([[1,2,3], [4,5,6]])
new_arr_2d = np.delete(arr_2d, 0, axis=0) #delete first position row at row wise

print(new_arr_2d)