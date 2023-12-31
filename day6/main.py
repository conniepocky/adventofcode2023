import numpy

with open("practise.txt", "r") as f:
  data = f.read().splitlines()

data[0] = data[0].replace("Time:", "")

times = list(map(int, data[0].split()))

data[1] = data[1].replace("Distance:", "")

distances = list(map(int, data[1].split()))

ways = []

for t in times:
    timeIndex = times.index(t)
    numberOfOptions = 0
    for timeHeld in range(0, t):
        d = timeHeld * (t-timeHeld)
        if d > distances[timeIndex]:
            numberOfOptions += 1
    ways.append(numberOfOptions)

print(numpy.prod(ways))