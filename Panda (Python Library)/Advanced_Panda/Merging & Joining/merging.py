# Syntax -> pd.merge(df1, df2, on="Column_Name", how="type of join")
import pandas as pd

# customer dataframe
df_customers = pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ['Ramesh', 'Suresh', 'Kalpesh'],
})

# order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1,2,4],
    'OrderAmount': [250, 450, 350]
})

# merge   #on -> common column name   #how -> type of join
df_merged = pd.merge(df_customers, df_orders, on='CustomerID', how='inner') # inner or right or etc
print('inner join')
print(df_merged)

"""
1df = m rows
2df = n rows
3df = m*n rows
"""