# Sports Data Pipeline

## Goal
[One sentence: e.g. "Collect, clean, and merge football match data 
from multiple sources to analyze how scoring trends have changed 
over the last decade."]

## Question I'm answering
[e.g. "How has average goals-per-match changed across the last 10 
Premier League seasons?"]

## Data sources
- [ ] API — football-data.org (recent match/standings data)
- [ ] Scraping — Wikipedia (historical season tables)
- [ ] Bulk CSV — football-data.co.uk (historical match-by-match data)

## Architecture
Raw data (local/S3) → Cleaned + merged (pandas) → Postgres → Analysis

## Tools used
Python, Rust, AWS (S3, RDS, Lambda), PostgreSQL, Docker

## Status
Day 4 — all three raw collection methods complete (API, scraping, bulk CSV).

## Progress log
- Day 1: Initialized repo, folder structure, README, .gitignore.
- Day 2: Built scripts/collect/fetch_api_data.py — pulls 2023-24 
  Premier League matches from football-data.org API, validates 
  response status, saves raw JSON to raw/api/.
- Day 3: Built scripts/collect/scrape_table.py — scrapes the 
  2023-24 Premier League final standings table from Wikipedia, 
  parses it with BeautifulSoup, saves raw JSON to raw/scrape/.
- Day 4: Built scripts/collect/load_bulk_csv.py — inspects FBref-style 
  match log CSV (760 rows, team-per-match format) for 2023-24 Premier 
  League season. Confirmed 20 teams, 38 matches each, only Notes 
  column has missing data.
  