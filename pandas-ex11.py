
import pandas as pd

data = {
    'department': ['Sales', 'Sales', 'IT', 'IT', 'HR', 'HR', 'Sales'],
    'name': ['Kim', 'Lee', 'Park', 'Choi', 'Jung', 'Han', 'Yoon'],
    'salary': [4500, 5200, 6000, 5800, 4200, 4000, 4800],
    'age': [28, 35, 40, 32, 29, 45, 31]
}

df = pd.DataFrame(data)
result = (
    df[df['salary'] >= 4500]
    .groupby('department', as_index=False)
    .agg(
        avg_salary=('salary', 'mean')
    )
)

print(result)
