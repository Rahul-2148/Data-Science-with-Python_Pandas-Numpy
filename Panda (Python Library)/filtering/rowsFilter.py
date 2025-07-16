import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, 23, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, 60000, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance_Score": [95, 90, 85, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)

high_salary = df[df['Salary'] > 50000]
print('Employees with salary > 50000')
print(high_salary)

# using AND & condition -> sari condition true honi chahiye isme
# filtering rows based on multiple conditions, Salary > 50000 & Age > 25
filtered = df[(df['Salary'] > 50000) & (df['Age'] > 25)]
print(f'Employee list Salary > 50000 & Age > 25')
print(filtered)

# using OR | condition -> koi ek bhi true ho toh chal jayega
# filtering rows based on multiple conditions, Age > 25 | Performance_Score > 80
filtered_or = df[(df['Age'] > 25) | (df['Performance_Score'] > 80)]
print(f'Employee list Age > 25 | Performance_Score > 80')
print(filtered_or)