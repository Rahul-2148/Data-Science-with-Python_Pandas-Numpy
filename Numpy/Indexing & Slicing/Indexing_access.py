"""
array[index] #1d array
array[row, column] #2d array
array[row, column, depth] #3d array
"""
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0]) #first element
print(arr[2]) #30 0 based
print(arr[-1]) #last element


'''
indexing aur slicing ke help se hm array ke kisi specific position pe ya koi bhi specific element ko access kr skte h. 

Indexing -> ka mtlb hota h ki single element ko select krna kisi bhi array me se 
           (access single element)

Slicing -> ka mtlb hota h multiple element ko select krna kisi bhi array me se
           (access multiple element)
           
fancy indexing -> multiple elements ko ek baar me select krna using indices as a list

Boolean Masking -> mtlb hm ek certain condition denge aur phir us hisab se element ko filter 
                   krenge. 
           
'''