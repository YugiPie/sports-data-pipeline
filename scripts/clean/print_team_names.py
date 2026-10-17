import json
import pandas as pd

# 1. Scraped standings (markers already in the team text, e.g. "Manchester City(C)")
with open("raw/scrape/pl_standings_2023_24.json", encoding="utf-8") as f:
    standings = json.load(f)

print("=== SCRAPED ===")
for row in standings:
    print(row["team"])

# 2. Bulk CSV (one row per team per match, so use unique values)
df = pd.read_csv("raw/bulk/matches.csv")

print("\n=== CSV ===")
for name in sorted(df["Team"].unique()):
    print(name)

# 3. API (team names are nested under homeTeam)
with open("raw/api/pl_matches_2023.json", encoding="utf-8") as f:
    api_data = json.load(f)

api_names = sorted({m["homeTeam"]["name"] for m in api_data["matches"]})

print("\n=== API ===")
for name in api_names:
    print(name)