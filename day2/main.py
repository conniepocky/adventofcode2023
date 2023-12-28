
with open("input.txt", "r") as f:
  data = f.read().splitlines()

games = []

successfulGames = []

for line in data:
    game = line.split(";")

    first = game[0].split(":")[1]

    game[0] = game[0].split(":")[0]

    game.insert(1, first)

    games.append(game)

for i in range(0, len(games)):
    currentGame = int(games[i][0].split("Game")[1].strip())

    entireGameWorks = True

    for f in range(1, len(games[i])):

        works = False

        temp = games[i][f].replace(" ", "")
        temp = temp.split(",")

        for t in temp:
            num = ""
            for c in t:
                if c.isnumeric():
                    num += c
                
            t = t.split(num)
            num = int(num)

            print(t, num)

            if t[1] == "red" and num <= 12:
                works = True
            elif t[1] == "blue" and num <= 14:
                works = True
            elif t[1] == "green" and num <= 13:
                works = True
            else:
                works = False
                entireGameWorks = False

    if entireGameWorks:
        successfulGames.append(currentGame)
    

print(sum(successfulGames))


