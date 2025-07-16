import pandas as pd

data = {
    "Time": [1,2,3,4,5],
    "Value": [10, None, 30, None, 50]
}

df = pd.DataFrame(data)
print('Before Interpolation')
print(df)

df['Value'] = df['Value'].interpolate(method='linear')
print('After Interpolation')
print(df)


"""
Interpolation -> is a technique jiski help se jo missing values hoti h unme ek estimated values fill  
                 kr skte h numerical column ke andar.

Interpolation ka use kab krna h, jb -->
1- time series data (work on stock market data analysis)
2- numeric data (follow the trends in the data) (eg. sales data, temperature data, etc)
3- avoid dropping rows with missing values

Disadvantages:
1- doesn't work well with categorical data (eg. string data, boolean data, names, ids etc)
2- It assumes a predictable pattern which might not always exists
"""