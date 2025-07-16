import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, 23, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, 60000, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance Score": [95, 90, 85, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)

# diplay the dataframe
print('Sample Dataframe')
print(df)

print("Names (single column return series)")
name = df["Name"]
print(name)

# selecting multiple columns
subset = df[["Name", "Salary"]] 
print('\nSubset with Name and Salary')
print(subset)