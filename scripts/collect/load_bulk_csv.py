import pandas as pd

df = pd.read_csv("raw/bulk/matches.csv")

print(f"Shape: {df.shape}")
print(f"Columns: {df.columns.tolist()}")
print(df.head())

print(f"Unique teams: {df['Team'].nunique()}")
print(df['Team'].value_counts())
print(df.isnull().sum())
