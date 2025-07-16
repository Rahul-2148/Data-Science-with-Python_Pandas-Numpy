#head() tail()
# head(n) -> display the last row of dataframe
#head() -> first 5 rows
#tail() -> last 5 rows

import pandas as pd

df = pd.read_json("Panda Library/files/sample_data.json")
print('Display 10 rows of first')
print(df.head(10))

print('Display 10 rows of last')
print(df.tail(10))