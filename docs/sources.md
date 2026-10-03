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