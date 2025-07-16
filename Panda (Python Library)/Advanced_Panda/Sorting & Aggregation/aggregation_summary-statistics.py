#Aggregation involves calculating summary statistics (calculate sum, findout mean, count value in entire dataframe) for a column of data.

#summary statistics provides numerical summaries of columns (like what is: avg. value, total value, min value, max value etc)

"""
df["Column Name"].mean()
df["Column Name"].sum()
df["Column Name"].min()
df["Column Name"].max()
"""

import pandas as pd

data = {
    "Name": ['Arun', 'Varun', 'Tarun'],
    "Age": [28, 34, 22],
    "Salary": [10000, 20000, 30000]
}

df = pd.DataFrame(data)

average_salary = df['Salary'].mean()
print(average_salary)