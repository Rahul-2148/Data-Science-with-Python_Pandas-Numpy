import pandas as pd

data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok"],
    "Age": [23, 24, 23, 25],
    "City": ["Koderma", "Saltora", "Durgapur", "Dhanwar"]
}

df = pd.DataFrame(data)
print(df)
# df.to_csv("Panda (Python Library)/files/output.csv", index=False)
# df.to_excel("Panda (Python Library)/files/output.xlsx", index=False)
df.to_json("Panda (Python Library)/files/output.json", orient="records")