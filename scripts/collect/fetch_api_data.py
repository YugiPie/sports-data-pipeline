import os
import json
from dotenv import load_dotenv
import requests

load_dotenv()
API_KEY = os.getenv("FOOTBALL_API_KEY")

uri = 'https://api.football-data.org/v4/competitions/PL/matches?season=2023'
headers = { 'X-Auth-Token': API_KEY }

def fetch_data(uri, headers):
    try:
        response = requests.get(uri, headers=headers)
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return

    if response.status_code != 200:
        print(f"Request failed with status {response.status_code}")
        print(response.text)
        return

    data = response.json()
    matches = data.get('matches', [])

    # quick sanity check in terminal
    for match in matches[:5]:
        home_team = match['homeTeam']['name']
        away_team = match['awayTeam']['name']
        print(f"{home_team} vs {away_team}")

    # save the full raw response
    os.makedirs("../../raw/api", exist_ok=True)
    output_path = "../../raw/api/pl_matches_2023.json"
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Saved {len(matches)} matches to {output_path}")

fetch_data(uri, headers)