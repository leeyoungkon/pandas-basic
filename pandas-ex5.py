import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Kim', 'Choi'],
    'age': [25, 30, 35, 25, 40],
    'city': ['Seoul', 'Busan', 'Daegu', 'Seoul', 'Incheon']
}

df = pd.DataFrame(data)
df = df.drop_duplicates()

print(df)
