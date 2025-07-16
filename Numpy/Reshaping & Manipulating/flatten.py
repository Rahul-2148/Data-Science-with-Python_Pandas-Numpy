"""
when you want to convert multi-dimensional array into 1D array then use flatten

.ravel() -> Returns a contiguous flattened array. -> views (original array will be changed)
.flatten() -> Returns a copy of the array collapsed into one dimension. -> copy (original array will not be changed)

chahe ravel() se karo ya flatten() se karo output same aayega sirf difference itna h ki ravel view h aur flatten copy h
"""
import numpy as np

arr_2d = np.array([[1,2,3], [4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())

# output
# [1 2 3 4 5 6] #ravel (view) (original array will be changed)
# [1 2 3 4 5 6] #flatten (copy) (original array will not be changed)

"""
indexing
slicing
fancy indexing
boolean masking
array shape 
ravel, flatten
"""
