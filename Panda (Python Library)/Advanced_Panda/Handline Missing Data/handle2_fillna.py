#fillna()
#fillna(value, inplace = True)

#axis 0 mtlb rows me missing value ko udana, axis 1 mtlb columns me missing value ko udana
#inplace = True -> change the original dataframe (not makes a copy of the dataframe)

import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', None, "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, None, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, None, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance Score": [95, 90, None, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)
print(df)

# filling with 0 -> df.fillna(0, inplace = True) 
# df.fillna(0, inplace = True) 
# print(df)

# filling with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)