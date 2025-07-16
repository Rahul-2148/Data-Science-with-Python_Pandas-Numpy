import pandas as pd

# read data from csv file into a dataframe
# df = pd.read_csv("Panda (Python Library)/files/mtcars-parquet.csv", encoding="utf-8")
# df = pd.read_excel("Panda (Python Library)/files/products.xlsx")
df = pd.read_json("Panda (Python Library)/files/sample_data.json")

print(df)
