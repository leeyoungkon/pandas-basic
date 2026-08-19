import pandas as pd

file_id = "1p_DI7muWd7wfntbZKMUCJWN4xyZMvQRn"
csv_url = f"https://drive.google.com/uc?id={file_id}"
df = pd.read_csv(csv_url)

print(df)


