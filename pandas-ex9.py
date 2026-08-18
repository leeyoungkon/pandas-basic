import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi'],
    'score': [85, 92, 78, 66],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu']
}

df = pd.DataFrame(data)

print(df)
df['country'] = 'Korea'
print(df)
df['result'] = df['score'] >= 60
print(df)
def grade(score):
  if score >= 80:
      return 'A'
  else:
      return 'B'

df['grade'] = df['score'].apply(grade)
print(df)
df['result'] = df['score'].apply(
    lambda x: 'Pass' if x >= 70 else 'Fail'
)
print(df)
df['name'] = df['name'].str.upper()

print(df)
df['name_length'] = df['name'].str.len()
print(df)
print(df[df['city'].str.contains('Seoul')])
