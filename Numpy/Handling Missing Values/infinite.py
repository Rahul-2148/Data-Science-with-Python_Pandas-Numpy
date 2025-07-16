'''
np.isinf() -> iska use infinite values ko detect karne ke liye hota hai
'''

# np.isinf() 10^1000
# 1/0

import numpy as np

arr = np.array([1, 2, np.inf, 4, np.inf, 6])

print(np.isinf(arr))

# output
# [False False  True False  True False]
