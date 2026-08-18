import pandas as pd

data = {
    "name": ["Kim", "Lee", "Park", "Choi", "Jung"],
    "age": [25, 32, 28, 41, 35],
    "salary": [3500, 4200, 3900, 5200, 4700],
    "department": ["IT", "HR", "IT", "Sales", "Sales"]
}

df = pd.DataFrame(data)

print(df)

print("=========")

print(df.isnull().sum())
print("=========")

print(df.loc[0, ["name", "salary"]])