#sorting data
# SORTING -> is the process of arranging data in a particular order.
# ascending order -> True , descending order -> False
#SORTING DATA 1 COLUMN sort_values()
# df.sort_values(by="Column Name", True/False, inplace=True)

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Tarun'],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)
print(df)

df.sort_values(by="Age", ascending=False, inplace=True)
print('Sorted Age in Descending Order')
print(df)