# By using python list comprehension, it is slow because it is not vectorized operation so we used numpy vectorization for faster execution.

list1 = [1,2,3]
list2 = [4,5,6]

result = [x + y for x, y in zip(list1, list2)] #here used python list comprehension
print(result)

# output
# [5, 7, 9]