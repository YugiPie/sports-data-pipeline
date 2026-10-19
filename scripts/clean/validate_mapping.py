# scripts/clean/validate_mapping.py
import json
import pandas as pd

api_df = pd.read_csv("data/clean/matches_api_clean.csv")

# 1. Matches per team: each team should appear 38 times (19 home + 19 away)
home_counts = api_df["home_team"].value_counts()
away_counts = api_df["away_team"].value_counts()
totals = home_counts.add(away_counts, fill_value=0).astype(int)
print("Matches per team:")
print(totals.sort_values())

# 2. Team set must match the standings file
with open("raw/scrape/pl_standings_2023_24.json", encoding="utf-8") as f:
    standings = json.load(f)

import sys
sys.path.append("scripts/clean")
from normalize_teams import normalize_team

standings_teams = {normalize_team(row["team"]) for row in standings}
match_teams = set(totals.index)

print("\nIn standings but not in matches:", standings_teams - match_teams or "none")
print("In matches but not in standings:", match_teams - standings_teams or "none")
print("Team count:", len(match_teams), "(expected 20)")