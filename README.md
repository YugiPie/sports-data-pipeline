# Sports Data Pipeline

## Goal
[One sentence: e.g. "Collect, clean, and merge football match data 
from multiple sources to analyze how scoring trends have changed 
over the last decade."]

## Question I'm answering
"What were the goals-per-match and key team stats for the 2023-24 Premier League season,
 and how do the three sources agree on them?"

 ## Data sources
   - [x] API — football-data.org (2023-24 PL matches)
   - [x] Scraping — Wikipedia (2023-24 PL final standings)
   - [x] Bulk CSV — Kaggle, https://www.kaggle.com/datasets/mertbayraktar/english-premier-league-matches-20232024-season

## Architecture
Raw data (local/S3) → Cleaned + merged (pandas) → Postgres → Analysis

## Tools used
Python and pandas, requests, BeautifulSoup

## Status
Day 5 — unified schema defined (matches + standings tables). Next: Week 2 cleaning.

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
- Day 5: Designed unified schema in docs/schema.md — matches table (one row per match) and standings table (one row per team per season).