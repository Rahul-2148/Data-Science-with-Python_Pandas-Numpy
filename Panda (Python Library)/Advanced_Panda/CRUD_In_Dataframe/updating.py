#updating values
import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok", "Anshika", "Neha", "Mudassar", "Ahmad", "Arbaz"],
    "Age": [23, 24, 23, 25, 26, 27, 28, 29, 30],
    "Salary": [150000, 80000, 60000, 84000, 65000, 55000, 10000, 20000, 30000],
    "Performance_Score": [95, 90, 85, 80, 75, 70, 65, 60, 55]
}

df = pd.DataFrame(data)
print(df)

# updating values 
#.loc[] -> ek method h panda me jiska use krke hm specific shell, set of rows, or columns ko access kr skte h aur phir usme modification kr skte h (loc stands for location or indexing)
# df.loc[row_index, "Column Name"] = new_value
df.loc[1, 'Salary'] = 90000
print(df)