'''
Numpy me aise kuch functions hote hain jo nan ko automatically ignore kar dete hain:

- `np.nanmean(arr)` → nan ignore karke average
- `np.nansum(arr)` → nan ignore karke sum
- `np.nanmax(arr)` → nan ignore karke max
- `np.nanmin(arr)` → nan ignore karke min

💡nan_to_num -> iska use missing values ko replace krne ke liye hota hai.
'''
 #Note: agar nan me kuch bhi paas nhi kroge toh default value 0 rahegi 
# np.nan_to_num(array, nan=value) default - 0 
import numpy as np

arr = np.array([1, 2, np.nan, 4, np.nan, 6])

cleaned_arr = np.nan_to_num(arr, nan=100)
print(cleaned_arr)