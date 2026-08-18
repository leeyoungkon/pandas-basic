import pandas as pd

data = {
    'product': ['A', 'B', 'C', 'D', 'E'],
    'price': [10000, 25000, -5000, 3000000, 15000],
    'stock': [10, 0, 20, -3, 5]
}

df = pd.DataFrame(data)
print(df)
print(df[df['price'] < 0])
print(df[df['stock'] < 0])
print(df[
    df['price'].between(0, 1000000)
])
df_clean = df[
    (df['price'].between(0, 1000000)) &
    (df['stock'] >= 0)
]
print(df_clean)