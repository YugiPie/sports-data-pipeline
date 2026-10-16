# Unified Schema

## Table: matches (grain: one row per match)

| Column | Type | From API | From Bulk CSV | Notes |
|---|---|---|---|---|
| match_id | string | generated from date + home + away | generated the same way | pairs the two CSV rows into one match |
| match_date | date | utcDate | Date | normalize to YYYY-MM-DD |
| season | string | fixed "2023-24" | fixed "2023-24" | |
| matchweek | int | not in response | Round | unreliable for sorting, use match_date |
| home_team | string | homeTeam.name | Team where Venue=Home | normalize names |
| away_team | string | awayTeam.name | Team where Venue=Away | normalize names |
| home_goals | int | score.fullTime.home | GF where Venue=Home | |
| away_goals | int | score.fullTime.away | GF where Venue=Away | |
| home_xg | float | not available | xG where Venue=Home | null for API-only matches |
| away_xg | float | not available | xG where Venue=Away | null for API-only matches |
| status | string | status | not in CSV | keep only FINISHED |


## Table: standings (grain: one row per team per season)

| Column | Type | From scraped | Notes |
|---|---|---|---|
| season | string | fixed "2023-24" | |
| position | int | Pos | |
| team | string | Team | strip (C) / (R) markers |
| played | int | Pld | |
| won | int | W | |
| drawn | int | D | |
| lost | int | L | |
| goals_for | int | GF | |
| goals_against | int | GA | |
| goal_diff | int | GD | strip the + / − sign |
| points | int | Pts | strip footnote markers like [c] |