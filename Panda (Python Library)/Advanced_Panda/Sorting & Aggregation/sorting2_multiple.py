# ascending order -> True , descending order -> False
# df.sort_values(by=["Age", "Salary"], ascending=True, inplace=True)

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Tarun'],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)
df.sort_values(by=["Age", "Salary"], ascending=[True, False], inplace=True)
print('Sorted Age in Ascending Order & Salary in Descending Order')
print(df)