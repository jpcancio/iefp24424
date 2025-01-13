import csv
import json

# Read CSV file
athletes = []
with open('atletas.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        athletes.append(row)

# Write JSON file
with open('atletas.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(athletes, jsonfile, ensure_ascii=False, indent=2)
