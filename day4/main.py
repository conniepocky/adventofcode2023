import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

totalPoints = []

for card in data:
    data[data.index(card)] = re.split(": |\| ", card)

for card in data:
    winningPoints = 0
    for i in card[1].split():
        if i in card[2].split():
            if winningPoints >= 1:
                winningPoints *= 2
            else:
                winningPoints += 1
    
    totalPoints.append(winningPoints)

print(sum(totalPoints))