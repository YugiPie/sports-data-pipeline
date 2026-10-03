import requests
import os
import json
from bs4 import BeautifulSoup


url = "https://en.wikipedia.org/wiki/2023%E2%80%9324_Premier_League"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print(f"Request failed with status {response.status_code}")
else:
    print(f"Success! Page length: {len(response.text)} characters")
  
    
#Number of wikitable class   
soup = BeautifulSoup(response.text, 'html.parser')

tables = soup.find_all('table', class_='wikitable')
print(f"Found {len(tables)} wikitable tables on this page")


#first row of each table
for i, t in enumerate(tables):
    first_row_text = t.find('tr').get_text(strip=True)
    print(f"Table {i}: {first_row_text[:80]}")
    
    
#Number of rows in table
league_table = tables[3]
rows = league_table.find_all('tr')
print(f"Found {len(rows)} rows")


#first 3 rows of table
standings = []

for row in rows:
    cells = row.find_all(['td', 'th'])
    cell_texts = [c.get_text(strip=True) for c in cells]
    
    # skip header row - check if first cell is a number
    if not cell_texts or not cell_texts[0].isdigit():
        continue
    
    team_data = {
        "position": cell_texts[0],
        "team": cell_texts[1],
        "played": cell_texts[2],
        "won": cell_texts[3],
        "drawn": cell_texts[4],
        "lost": cell_texts[5],
        "goals_for": cell_texts[6],
        "goals_against": cell_texts[7],
        "goal_diff": cell_texts[8],
        "points": cell_texts[9],
    }
    standings.append(team_data)

print(f"Parsed {len(standings)} team rows")
for s in standings[:3]:
    print(s)
    
    
#Saving the data in raw/scrape
os.makedirs("../../raw/scrape", exist_ok=True)

output_path = "../../raw/scrape/pl_standings_2023_24.json"
with open(output_path, "w") as f:
    json.dump(standings, f, indent=2)

print(f"Saved {len(standings)} rows to {output_path}")
