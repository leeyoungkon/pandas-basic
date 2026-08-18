import pandas as pd

data = {
    'order_id': [101, 102, 103, 101, 104, 105, 105],
    'product': ['A', 'B', 'C', 'A', 'B', 'C', 'C'],
    'price': [1000, 2000, 3000, 1000, 2000, 3000, 3000]
}
orders = pd.DataFrame(data)
print(orders)
print("중복 개수: "+str(orders.duplicated().sum()))
print(orders[orders.duplicated()])
print(orders[
    orders.duplicated(keep=False)
])
orders_clean = orders.drop_duplicates()
print(orders_clean)
