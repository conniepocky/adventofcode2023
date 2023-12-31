import numpy

with open("practise.txt", "r") as f:
  data = f.read().splitlines()

data[0] = data[0].replace("Time:", "")

time = int(data[0].replace(" ", ""))

data[1] = data[1].replace("Distance:", "")

distance = int(data[1].replace(" ", ""))

numberOfOptions = 0

for timeHeld in range(0, time):
    d = timeHeld * (time-timeHeld)
    if d > distance:
        numberOfOptions += 1

print(numberOfOptions)