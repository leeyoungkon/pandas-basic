import pandas as pd

data = {
    'email': [
        'kim@gmail.com',
        'lee@naver.com',
        'park@gmail.com'
    ]
}

df = pd.DataFrame(data)
#df['email'].str.split('@')
df['user_id'] = df['email'].str.split('@').str[0]
df['domain'] = df['email'].str.split('@').str[1]

print(df)