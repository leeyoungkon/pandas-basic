import pandas as pd

sales1 = pd.DataFrame({
    'year': [2025, 2025, 2026],
    'product': ['A', 'B', 'A'],
    'sales': [100, 200, 150]
})

sales2 = pd.DataFrame({
    'year': [2025, 2025, 2026],
    'product': ['A', 'B', 'A'],
    'price': [1000, 2000, 1100]
})
result = pd.merge(
    sales1,
    sales2,
    on=['year', 'product']
)

#print(result)
df1 = pd.DataFrame({
    'id': [1, 2],
    'name': ['Kim', 'Lee'],
    'score': [80, 90]
})

df2 = pd.DataFrame({
    'id': [1, 2],
    'score': [85, 95]
})
result1 = pd.merge(
    df1,
    df2,
    on='id'
)
#print(result1)
sales_jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 200]
})

sales_feb = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [150, 250]
})
result2 = pd.concat(
    [sales_jan, sales_feb],
    ignore_index=True
)

#print(result2)
df3 = pd.DataFrame({
    'name': ['Kim', 'Lee', 'Park']
})

df4 = pd.DataFrame({
    'score': [80, 90, 85]
})
result3 = pd.concat(
    [df3, df4],
    axis=1
)

#print(result3)
df5 = pd.DataFrame({
    'name': ['Kim', 'Lee'],
    'score': [80, 90]
})

df6 = pd.DataFrame({
    'name': ['Park', 'Choi'],
    'age': [30, 35]
})
result4 = pd.concat(
    [df5, df6],
    ignore_index=True
)

print(result4)


