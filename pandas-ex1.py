import pandas as pd

data = {
    "product": ["A100", "A200", "A300"],
    "stock": [15, 120, -5],
    "price": [85000, 25000, 35000]
}

df = pd.DataFrame(data) 
df = df[df["stock"] >= 0]

print(df)
#print(df.shape)
