# importing necessary libraries
import pandas as pd
import numpy as np

# loading the dataset
df = pd.read_csv('Numpy/Indian Employee Dataset_Project/Corrupted_Indian_employees_data.csv')
print(df.head())

# checking the missing values
print('Missing Values in each column')
print(df.isnull().sum())

# fill missing numeric values
df['Salary (INR)'] = df['Salary (INR)'].fillna(df['Salary (INR)'].mean())
df['Performance Rating'] = df['Performance Rating'].fillna(df['Performance Rating'].median())

# detect infinite values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# fill remaining numeric missing values
df.fillna(df.mean(numeric_only=True), inplace=True)

# for categorical columns, fill missing with 'Unknown'
df['City'] = df['City'].fillna('Unknown')
df['Department'] = df['Department'].fillna('Unknown')

# remove duplicate records
df.drop_duplicates(inplace=True)

# replace negative salaries with mean salary
df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])

# remove unrealistic salaries (3 standard deviations rule)
salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3 * salary_std)
df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# save cleaned data
df.to_csv('Numpy/Indian Employee Dataset_Project/cleaned_Indian_Employee_Data.csv', index=False)

print('Data cleaning completed! Saved as "cleaned_Indian_Employee_Data.csv"')
