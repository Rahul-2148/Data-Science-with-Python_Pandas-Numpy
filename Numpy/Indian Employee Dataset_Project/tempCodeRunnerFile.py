df['Salary (INR)'].fillna(df['Salary (INR)'].mean(), inplace=True)

# df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace=True)

# df.replace([np.inf, -np.inf], np.nan, inplace=True)

# df.fillna(df.mean(), implace=True)

# # remove duplicate records
# df.drop_duplicates(inplace=True)

# # replace negative salaries
# df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean(), df['Salary (INR)'])

# salary_mean = df['Salary (INR)'].mean()
# salary_std = df['Salary (INR)'].std()
# lower_bound = salary_mean - (3 * salary_std)
# upper_bound = salary_mean + (3 * salary_std)

# # remove rows where salary is too high or too low
# df = df[(df['Salary (INR)'] >= lower_bound) & (df['Salary (INR)'] <= upper_bound)]

# df.to_csv('cleaned_Indian_Employee_Data.csv', index=False)

# print('Data cleaning completed! Saved as "cleaned_Indian_Employee_Data.csv"')