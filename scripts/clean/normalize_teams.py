# scripts/clean/normalize_teams.py
import json
import pandas as pd

# raw spelling -> canonical name
TEAM_MAP = {
    # Arsenal
    "Arsenal": "Arsenal",
    "Arsenal FC": "Arsenal",

    # Aston Villa
    "Aston Villa": "Aston Villa",
    "Aston Villa FC": "Aston Villa",
    "AstonVilla": "Aston Villa",

    # AFC Bournemouth
    "Bournemouth": "AFC Bournemouth",
    "AFC Bournemouth": "AFC Bournemouth",

    # Brentford
    "Brentford": "Brentford",
    "Brentford FC": "Brentford",

    # Brighton & Hove Albion
    "Brighton & Hove Albion": "Brighton & Hove Albion",
    "Brighton & Hove Albion FC": "Brighton & Hove Albion",
    "BrightonandHoveAlbion": "Brighton & Hove Albion",

    # Burnley
    "Burnley": "Burnley",
    "Burnley FC": "Burnley",
    "Burnley(R)": "Burnley",

    # Chelsea
    "Chelsea": "Chelsea",
    "Chelsea FC": "Chelsea",

    # Crystal Palace
    "Crystal Palace": "Crystal Palace",
    "Crystal Palace FC": "Crystal Palace",
    "CrystalPalace": "Crystal Palace",

    # Everton
    "Everton": "Everton",
    "Everton FC": "Everton",

    # Fulham
    "Fulham": "Fulham",
    "Fulham FC": "Fulham",

    # Liverpool
    "Liverpool": "Liverpool",
    "Liverpool FC": "Liverpool",

    # Luton Town
    "Luton Town": "Luton Town",
    "Luton Town FC": "Luton Town",
    "Luton Town(R)": "Luton Town",
    "LutonTown": "Luton Town",

    # Manchester City
    "Manchester City": "Manchester City",
    "Manchester City FC": "Manchester City",
    "Manchester City(C)": "Manchester City",
    "ManchesterCity": "Manchester City",

    # Manchester United
    "Manchester United": "Manchester United",
    "Manchester United FC": "Manchester United",
    "ManchesterUnited": "Manchester United",

    # Newcastle United
    "Newcastle United": "Newcastle United",
    "Newcastle United FC": "Newcastle United",
    "NewcastleUnited": "Newcastle United",

    # Nottingham Forest
    "Nottingham Forest": "Nottingham Forest",
    "Nottingham Forest FC": "Nottingham Forest",
    "NottinghamForest": "Nottingham Forest",

    # Sheffield United
    "Sheffield United": "Sheffield United",
    "Sheffield United FC": "Sheffield United",
    "Sheffield United(R)": "Sheffield United",
    "SheffieldUnited": "Sheffield United",

    # Tottenham Hotspur
    "Tottenham Hotspur": "Tottenham Hotspur",
    "Tottenham Hotspur FC": "Tottenham Hotspur",
    "TottenhamHotspur": "Tottenham Hotspur",

    # West Ham United
    "West Ham United": "West Ham United",
    "West Ham United FC": "West Ham United",
    "WestHamUnited": "West Ham United",

    # Wolverhampton Wanderers
    "Wolverhampton Wanderers": "Wolverhampton Wanderers",
    "Wolverhampton Wanderers FC": "Wolverhampton Wanderers",
    "WolverhamptonWanderers": "Wolverhampton Wanderers",
}


def normalize_team(name):
    if name in TEAM_MAP:
        return TEAM_MAP[name]
    print(f"WARNING: no mapping for '{name}'")
    return name


if __name__ == "__main__":
    # 1. Scraped standings
    with open("raw/scrape/pl_standings_2023_24.json", encoding="utf-8") as f:
        standings = json.load(f)
    scraped_names = [row["team"] for row in standings]

    # 2. Bulk CSV
    df = pd.read_csv("raw/bulk/matches.csv")
    csv_names = df["Team"].unique()

    # 3. API
    with open("raw/api/pl_matches_2023.json", encoding="utf-8") as f:
        api_data = json.load(f)
    api_names = {m["homeTeam"]["name"] for m in api_data["matches"]} | {
        m["awayTeam"]["name"] for m in api_data["matches"]
    }

    # Run every name through the normalizer
    all_names = set(scraped_names) | set(csv_names) | api_names
    for name in sorted(all_names):
        normalize_team(name)

    # Final check: every canonical name should be one of the 20 teams
    canonical = {normalize_team(n) for n in all_names}
    print(f"\nCanonical teams found: {len(canonical)} (expected 20)")
    for team in sorted(canonical):
        print(" -", team)