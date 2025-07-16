'''
Vectorization in Numpy is a way to apply a function to all elements of an array at once.

it is 100x faster than using a for loop to iterate over the array and apply the function to each element.
'''
# Vectorization Addition
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

result = arr1 + arr2
print(result)