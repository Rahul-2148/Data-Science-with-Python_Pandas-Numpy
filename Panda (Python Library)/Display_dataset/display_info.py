import pandas as pd 

# df = pd.read_json("Panda Library/files/sample_data.json")
data = {
    "Name": ['Rahul', 'Sujay', 'Suman', "Alok"],
    "Age": [23, 24, 23, 25],
    "City": ["Koderma", "Saltora", "Durgapur", "Dhanwar"]
}

df = pd.DataFrame(data)

print('Displaying the info of data set')
print(df.info())