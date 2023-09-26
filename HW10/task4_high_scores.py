import csv

# Reading data from scores.csv
with open("scores.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile)
    player_scores = {}

    for row in csvreader:
        player = row[0]
        score = int(row[1])

        if player not in player_scores or score > player_scores[player]:
            player_scores[player] = score

# Save to high_scores.csv
with open("high_scores.csv", "w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile)
    for player, score in sorted(player_scores.items(),
                                key=lambda x: x[1], reverse=True):
        csvwriter.writerow([player, score])
