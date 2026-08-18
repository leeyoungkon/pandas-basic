import pandas as pd
import numpy as np

data = {
    "name": ["Kim", "Lee", "Park", "Choi", "Jung"],
    "age": [25, 32, np.nan, 41, 35],
    "salary": [3500, np.nan, 3900, 5200, 4700],
    "department": ["IT", "HR", "IT", None, "Sales"]
}

df = pd.DataFrame(data)

#print(df)

print(df.dropna())