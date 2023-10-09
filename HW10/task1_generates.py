import random

# Generates and random number
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    with open(f"{char}.txt", "a") as file:
        random_number = random.randint(1, 100)
        file.write(str(random_number) + "\n")

# summary.txt
with open("summary.txt", "w") as summary_file:
    for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        with open(f"{char}.txt", "r") as file:
            content = file.read().strip()
            summary_file.write(f"{char}.txt: {content}\n")
