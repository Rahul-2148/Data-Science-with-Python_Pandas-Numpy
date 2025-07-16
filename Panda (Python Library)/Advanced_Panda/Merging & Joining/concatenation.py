"""
vertically concatenate (row-wise)
horizontally concatenate (column-wise)

pd.concat([df1, df2], axis=0, ignore_index=True)

[df1, df2] = 

axis = 0 -> vertically concatenate (row-wise)
axis = 1 -> horizontally concatenate (column-wise)

ignore_index = True -> reset the index
"""

# combining 2 dataframes vertically
import pandas as pd

# region 1
df_Region1 = pd.DataFrame({
    'CustomerID': [1,2],
    'Name': ['Gopal', 'Raju']
})

# region 2  
df_Region2 = pd.DataFrame({
    'CustomerID': [3,4],
    'Name': ['Shyam', 'Baburao']
})

# concatenate vertically (axix = 0 default le leta h agar axis paas nahi kro)
df_concat = pd.concat([df_Region1, df_Region2], axis=0, ignore_index=True)
print(df_concat)