import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park'],
    'age': [25, 30, 28],
    'score': [85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
df.to_csv('result.csv')
