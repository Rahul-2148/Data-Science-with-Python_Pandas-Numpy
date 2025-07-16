# adding columns
import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, 23, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, 60000, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance_Score": [95, 90, 85, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)
# square brackets df["Column_Name"] = some_Data (some data means us column me data me list, series or calculations ho sakti h)

print(df)

df["Bonus"] = df["Salary"] * 0.1
print(df)

df["Total_Salary"] = df["Salary"] + df["Bonus"]
print(df)

# using insert() method to add a new column at a specific position
#df.insert(loc, "Column_Name", some_data)
df.insert(0, "Employee ID", [10, 20, 30, 40, 50, 60, 70, 80, 90])
print(df) 