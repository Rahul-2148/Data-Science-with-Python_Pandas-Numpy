"""
1- how big is your data set
2- what are the names of the columns

shape is a attribute that returns tuple with 2 values (rows, columns)
columns is a attribute that returns list of column names
"""

import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, 23, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, 60000, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance Score": [95, 90, 85, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)
print(df)
print(f'Shape: {df.shape}') #f -> format string
print(f'Column Names: {df.columns}')

"""
(10000, 20)
(5, 4)
"""