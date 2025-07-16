import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Tarun', "Karun", "Nandini"],
    "Age": [28, 34, 22, 34, 28],
    "Salary": [50000, 60000, 45000, 52000, 48000]
}

df = pd.DataFrame(data)
grouped = df.groupby("Age")["Salary"].sum()
print(grouped)

"""
data ko group krke aggregation apply kr diya
df.groupby("Age")
age = 22 > [45000]
age = 28 [50000, 48000]
age = 34 [60000, 52000]

aggregation -> [Salary].sum()
age = 22 [45000]
age = 28 [50000 + 48000] = 98000
age = 34 [60000 + 52000] = 112000
"""