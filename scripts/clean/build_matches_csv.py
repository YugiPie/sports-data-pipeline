import sys
sys.path.append("scripts/clean")
import pandas as pd
from normalize_teams import normalize_team

df=pd.read_csv('raw/bulk/matches.csv')

df = df[df['Venue'] == 'Home'].copy()

df['Team']=df['Team'].apply(normalize_team)
df['Opponent']=df['Opponent'].apply(normalize_team)

df = df[['Date', 'Team', 'Opponent', 'GF', 'GA', 'Result', 'Attendance', 'Referee']]
df = df.rename(columns={
    'Date': 'match_date',
    'Team': 'home_team',
    'Opponent': 'away_team',
    'GF': 'home_goals',
    'GA': 'away_goals',
    'Result': 'home_result',
})

print(df.shape)
print(df.head())
print(df.isnull().sum())

import os
os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/matches_csv_clean.csv", index=False)
print("Saved", len(df), "rows to data/clean/matches_csv_clean.csv")