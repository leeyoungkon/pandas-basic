
import pandas as pd

students = pd.DataFrame({
    'student_id': [1, 2, 3, 4],
    'name': ['Kim', 'Lee', 'Park', 'Choi']
})

scores = pd.DataFrame({
    'student_id': [1, 2, 3],
    'score': [90, 80, 85]
})
result = pd.merge(
    students,
    scores,
    on='student_id',
    how='left'
)
#print(result)
products = pd.DataFrame({
    'product_id': ['A', 'B', 'C'],
    'product_name': ['Keyboard', 'Mouse', 'Monitor']
})

sales1 = pd.DataFrame({
    'product_id': ['A', 'B'],
    'quantity': [10, 20]
})

sales2 = pd.DataFrame({
    'product_id': ['A', 'C'],
    'quantity': [15, 5]
})
sales = pd.concat(
    [sales1, sales2],
    ignore_index=True
)
result2 = pd.merge(
    sales,
    products,
    on='product_id',
    how='left'
)
result3 = (
    result2.groupby(
        'product_id',
        as_index=False
    )
    .agg(
        total_quantity=('quantity', 'sum')
    )
    .sort_values(
        'total_quantity',
        ascending=False
    )
)
print(result3)