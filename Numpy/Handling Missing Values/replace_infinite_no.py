'''
🔥posinf -> positive infinity -> refers to the value of infinity (positive infinity) in mathematics. It represents the largest possible number in a real number system.
eg. 10^1000

🔥neginf -> negative infinity -> refers to the value of infinity (negative infinity) in mathematics. It represents the smallest possible number in a real number system.
eg. -10^1000
'''

# np.isinf() 10^1000
# 1/0

import numpy as np

arr = np.array([1, 2, np.inf, 4, np.inf, 6])

print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf=1000, neginf=-1000) 
print(cleaned_arr)

# output
# [False False  True False  True False]
# [  1.   2. 1000.   4. 1000.   6.]