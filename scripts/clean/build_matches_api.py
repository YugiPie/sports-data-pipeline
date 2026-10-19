# scripts/clean/build_matches_api.py
# Turns the football-data.org API response into one row per match,
# using the same column names as the CSV cleaning output.
import sys
sys.path.append("scripts/clean")

import json
import os

import pandas as pd
from normalize_teams import normalize_team

# Part A: load and count
with open("raw/api/pl_matches_2023.json", encoding="utf-8") as f:
    data = json.load(f)

matches = data["matches"]
print("Raw matches:", len(matches))

# Part B: keep only finished matches
finished = [m for m in matches if m["status"] == "FINISHED"]
print("Finished matches:", len(finished))

# Part C: pull out the columns
rows = []
for m in finished:
    rows.append({
        "match_date": m["utcDate"][:10],
        "home_team": normalize_team(m["homeTeam"]["name"]),
        "away_team": normalize_team(m["awayTeam"]["name"]),
        "home_goals": m["score"]["fullTime"]["home"],
        "away_goals": m["score"]["fullTime"]["away"],
    })

df = pd.DataFrame(rows)

# Part D: check and save
print("Shape:", df.shape)
print(df.head())
print(df.isnull().sum())

os.makedirs("data/clean", exist_ok=True)
df.to_csv("data/clean/matches_api_clean.csv", index=False)
print("Saved", len(df), "rows to data/clean/matches_api_clean.csv")