import pandas as pd

data = {
    "name": ["Kim", "Lee", "Park", "Choi", "Jung"],
    "age": [25, 32, 28, 41, 35],
    "salary": [3500, 4200, 3900, 5200, 4700],
    "department": ["IT", "HR", "IT", "Sales", "Sales"]
}

df = pd.DataFrame(data)

print(df)
print(df.head()) # Display the first 5 rows of the DataFrame
print(df.tail()) # Display the last 5 rows of the DataFrame

print(df.isnull().sum()) # Check for missing values in each column
print(df.info())  # Display a concise summary of the DataFrame

print(df.loc[0, ["name", "salary"]])  # Access the "name" and "salary" columns for the first row