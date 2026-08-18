import pandas as pd
import numpy as np

data = {
    "name": ["Kim", "Lee", "Park", "Choi"],
    "age": [25, 32, np.nan, 41],
    "salary": [3500, np.nan, 3900, 5200],
    "department": ["IT", "HR", "IT", None]
}

df = pd.DataFrame(data)

# 결측치 확인
print(df.isnull().sum())

# age는 평균으로 채우기
df["age"] = df["age"].fillna(
    df["age"].mean()
)

# salary는 중앙값으로 채우기
df["salary"] = df["salary"].fillna(
    df["salary"].median()
)

# department는 Unknown으로 채우기
df["department"] = df["department"].fillna(
    "Unknown"
)

print(df)