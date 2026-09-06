import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Kim', 'Choi'],
    'age': [25, 30, 35, 25, 40],
    'city': ['Seoul', 'Busan', 'Daegu', 'Seoul', 'Incheon']
}

df = pd.DataFrame(data)

print(df)  # Display the original DataFrame before dropping duplicates
#df = df[0:3]  # Select the first three rows of the DataFrame
#df = df.loc[0:3] # Select rows from index 0 to 3 (inclusive) using .loc
#df = df["name"]  # Select only the "name" column of the DataFrame
#df = df.drop_duplicates()
df = df.iloc[0:3,0:2]  # Select the first three rows and the first two columns using .iloc
print(df)
