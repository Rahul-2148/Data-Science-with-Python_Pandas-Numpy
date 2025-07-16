'''
error tb aata h ki ye automatically reshape nhi hoga, agar ek array me 2D aur ek 1D array h toh 1D me reshape krna hoga.
'''

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]]) #shape (2, 3)
arr2 = np.array([1,2]) #shape (2,)

result = arr1 + arr2

print(result)

#.reshape() -> changes shape 