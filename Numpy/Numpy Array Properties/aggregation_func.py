#aggregation -> calculate sum, findout mean, count value in entire dataframe

import numpy as np

arr = np.array([10, 20, 30, 40,50])

print(np.sum(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))


'''
Functions           what it does
np.sum(array)  ->   Returns the sum of all elements in the array
np.mean(array) ->   Calculates the average of all elements in the array
np.min(array)  ->   Returns the minimum value in the array
np.max(array)  ->   Returns the maximum value in the array
np.std(array)  ->   Returns the standard deviation of all elements in the array
np.var(array)  ->   Returns the variance of all elements in the array

standard deviation = square root of variance 

variance = average of the squared differences between each data point and the mean method

'''