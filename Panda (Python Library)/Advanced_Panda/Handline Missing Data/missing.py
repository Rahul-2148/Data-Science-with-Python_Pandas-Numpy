import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', None, "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, None, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, None, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance Score": [95, 90, None, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)
print(df)

print(df.isnull().sum())