file = open("input.txt", "r")

longData = file.read()

data = longData.split("\n")

numbers = []

for i in data:
    num = ""
    for c in i:
        if c.isnumeric():
            num += c
            break
    for c in i[::-1]:
        if c.isnumeric():
            num += c
            break
    
    if num.isnumeric():
        numbers.append(int(num))

print(sum(numbers))
