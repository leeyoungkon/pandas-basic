import pandas as pd

sales = pd.DataFrame({
    'region': ['Seoul', 'Busan', 'Seoul', 'Daegu', 'Busan', 'Seoul'],
    'product': ['A', 'A', 'B', 'A', 'B', 'A'],
    'amount': [100, 150, 200, 120, 180, 130]
})

#sales = sales.sort_values(by='amount')
#sales = sales.groupby('region', as_index=False).agg(total_amount=('amount', 'sum'))
#result = sales.groupby('region', as_index=False)['amount'].mean().rename(columns={'amount': 'avg_amount'})
#result = sales.groupby('region', as_index=False).agg(
#    avg_amount=('amount', 'mean'),
#    sum_amount=('amount', 'sum'),
#    max_amount=('amount', 'max'),
#    min_amount=('amount', 'min')
#)
result = sales.groupby('region', as_index=False).agg(
    avg_amount=('amount', 'mean')).sort_values(by='avg_amount', ascending=False)

print(result)