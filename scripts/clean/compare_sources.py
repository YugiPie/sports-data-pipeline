# scripts/clean/compare_sources.py
# Cross-checks the cleaned CSV output against the cleaned API output.
import pandas as pd

csv_df = pd.read_csv("data/clean/matches_csv_clean.csv")
api_df = pd.read_csv("data/clean/matches_api_clean.csv")

keys = ["match_date", "home_team", "away_team"]

merged = csv_df.merge(api_df, on=keys, how="inner", suffixes=("_csv", "_api"))
print("Matched:", len(merged), "of", len(csv_df), "CSV rows and", len(api_df), "API rows")

diff = merged[
    (merged["home_goals_csv"] != merged["home_goals_api"])
    | (merged["away_goals_csv"] != merged["away_goals_api"])
]

print("Differing matches:", len(diff))
if len(diff) > 0:
    print(diff[keys + ["home_goals_csv", "home_goals_api", "away_goals_csv", "away_goals_api"]])
    
