import pandas as pd

employees = pd.DataFrame({
    'emp_id': [101, 102, 103, 104],
    'name': ['Kim', 'Lee', 'Park', 'Choi'],
    'dept_code': [10, 20, 10, 50]
})

departments = pd.DataFrame({
    'dept_id': [10, 20, 30, 40],
    'department': ['Sales', 'IT', 'HR', 'Finance']
})

#print(employees)
#print(departments)

result = pd.merge(
    employees,
    departments,
    left_on='dept_code',
    right_on='dept_id',
    how='inner'
)

print(result)