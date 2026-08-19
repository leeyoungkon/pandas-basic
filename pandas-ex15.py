
import pandas as pd

customers = pd.DataFrame({
    'customer_id': [1, 2, 3],
    'name': ['Kim', 'Lee', 'Park']
})
orders = pd.DataFrame({
    'order_id': [1001, 1002, 1003],
    'customer_id': [1, 1, 2],
    'amount': [50000, 30000, 70000]
})
result = pd.merge(
    orders,
    customers,
    on='customer_id'
)
summary = (
    result.groupby(
        'name',
        as_index=False
    )
    .agg(
        total_amount=('amount', 'sum')
    )
)

#print(summary)

jan = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [100, 200]
})

feb = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [150, 250]
})

mar = pd.DataFrame({
    'product': ['A', 'B'],
    'sales': [180, 300]
})
sales = pd.concat(
    [jan, feb, mar],
    ignore_index=True
)

print(sales)
result2 = (
    sales.groupby(
        'product',
        as_index=False
    )
    .agg(
        total_sales=('sales', 'sum')
    )
)

print(result2)
