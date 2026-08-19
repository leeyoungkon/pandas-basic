import pandas as pd

data = {
    'name': ['Kim', 'Lee', 'Park'],
    'age': [25, 30, 28],
    'score': [85, 90, 88]
}

df = pd.DataFrame(data)

#print(df)
#df.to_csv('result.csv')

import pandas as pd

data = {
    '이름': ['김철수', '이영희', '박민수'],
    '부서': ['영업', '개발', '인사'],
    '점수': [85, 92, 78]
}

df = pd.DataFrame(data)

df.to_json(
    'result.json',
    orient='records',
    force_ascii=False
)