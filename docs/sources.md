   ## API — football-data.org
   - Base URL: https://api.football-data.org/v4/
   - Endpoint: /competitions/PL/matches
   - Auth: header `X-Auth-Token: <key>`
   - Season filter: ?season=2023 (format: 4-digit start year, e.g. 2023 = 2023-24 season)
   - Rate limit: 10 API calls per minute
   - Response shape:
     - Top-level keys: filters, resultSet, competition, matches
     - Each match object: homeTeam.name, awayTeam.name, 
       score.fullTime.home, score.fullTime.away, utcDate, status