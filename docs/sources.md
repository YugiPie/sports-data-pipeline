## API — football-data.org

- Base URL: https://api.football-data.org/v4/
- Endpoint: /competitions/PL/matches
- Auth: header `X-Auth-Token: <key>` (key stored in .env, never committed)
- Season filter: ?season=2023 (format: 4-digit start year = start of season, e.g. 2023 = 2023-24)
- Rate limit: 10 API calls per minute
- Response shape:
  - Top-level keys: filters, resultSet, competition, matches
  - Each match object: homeTeam.name, awayTeam.name, 
    score.fullTime.home, score.fullTime.away, utcDate, status
- Script: scripts/collect/fetch_api_data.py
- Output: raw/api/pl_matches_2023.json (gitignored, not committed)


 ## Scraping — Wikipedia (2023-24 Premier League season page)
 
  - URL: https://en.wikipedia.org/wiki/2023-24_Premier_League
  - Table: index 3 of 13 wikitable-class tables on the page
  - Columns extracted: position, team, played, won, drawn, lost, 
     goals_for, goals_against, goal_diff, points
  - Note: team names may include markers like (C) champion, (R) relegated
  - Script: scripts/collect/scrape_table.py
  - Output: raw/scrape/pl_standings_2023_24.json


## 3. Bulk CSV — FBref-style match logs (2023-24 Premier League)

- **Source**: Kaggle
-**LINK**:https://www.kaggle.com/datasets/mertbayraktar/english-premier-league-matches-20232024-season
- **File**: `raw/bulk/matches.csv`
- **Shape**: 760 rows × 28 columns
- **Structure**: ONE ROW PER TEAM PER MATCH, not one row per match —
  every match appears twice (once from each team's perspective).
  Confirmed: 20 unique teams, 38 matches each (760 = 20 × 38).
- **Columns of interest**: `Date`, `Round` (matchweek), `Venue` (Home/Away),
  `Result` (W/D/L), `GF`/`GA` (goals for/against), `xG`/`xGA` (expected goals),
  `Poss` (possession %), `Sh`/`SoT` (shots/shots on target), `Team`, `Opponent`
- **Columns to drop during cleaning**:
  - `Unnamed: 0` — leftover index column from original export, no real data
  - `Notes` — 100% null across all 760 rows, carries no information
- **Team name format**: no spaces/separators, e.g. `"ManchesterCity"`,
  `"SheffieldUnited"` — different style from both other sources
- **Date format**: ISO-like (`YYYY-MM-DD`, e.g. `2023-08-11`)
- **Known issue**: `Round` (matchweek number) doesn't always match
  chronological date order — rearranged/postponed fixtures keep their
  original matchweek label despite being played later. Same pattern
  independently observed in another bulk CSV explored during Day 4 —
  appears to be a general real-world football scheduling quirk, not
  a one-off data error.
- **Script**: `scripts/collect/load_bulk_csv.py`
- **Output**: inspected only — the file itself is the raw data, no
  separate save step needed
