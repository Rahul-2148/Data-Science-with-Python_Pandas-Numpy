'''
axis=0 -> row wise
axis=1 -> column wise
axis=None -> default (isme array ke flatten version me elements ko insert kr dega)
'''

import numpy as np

arr_2d = np.array([[1,2], [3,4]])
print(arr_2d)

print('Showing new 2d array')
# insert a new row at index 1
new_arr_2d = np.insert(arr_2d, 1, [5, 6], axis=None) #inserting [5, 6] at position 1 at column wise

print(new_arr_2d)