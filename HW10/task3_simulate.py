import csv
import random

# Game simulation
players = ["Josh", "Luke", "Kate", "Mark", "Mary"]
scores = []

for player in players:
    for _ in range(100):
        scores.append([player, random.randint(0, 1000)])

# Save to CSV file
with open("scores.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(scores)
