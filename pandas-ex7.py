import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park', 'Choi'],
    'city': ['Seoul', 'Busan', 'Seoul', 'Daegu'],
    'score': [110, 85, 88, -10]
}

df = pd.DataFrame(data)

print(df[
    df['city'].isin(['Seoul', 'Busan'])
])

import numpy as np

df.loc[
    ~df['score'].between(0, 100),
    'score'
] = np.nan
print(df)
