import json

with open("raw/api/pl_matches_2023.json", encoding="utf-8") as f:
    data = json.load(f)

print(len(data["matches"]), "matches")
print(json.dumps(data["matches"][0], indent=2))