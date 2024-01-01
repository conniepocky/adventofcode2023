import re

with open("input.txt", "r") as f:
    data = f.read().splitlines()

result = []

for card in data:
    data[data.index(card)] = re.split(": |\| ", card)

copies = {}

for card in data:
    copies.update({data.index(card)+1: 1})

copiesPerCard = []

for card in data:
    cardNum = int(data.index(card)+1)
    winningcopies = 0
    for i in card[1].split():
        if i in card[2].split():
            winningcopies += 1
    
    copiesPerCard.append(list(range(cardNum+1, cardNum+winningcopies+1)))

for card in copies:
    for i in range(0, card):
        print(copiesPerCard[i])
        if card in copiesPerCard[i]:
            copies[card] += (1 * copies[i+1])
    

for i in copies:
    result.append(copies[i])

print(sum(result))