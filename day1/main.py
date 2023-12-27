import re

file = open("input.txt", "r")

longData = file.read()

data = longData.split("\n")

wordNums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

numbers = []

for i in data:

    num = ""

    nums = []

    indexOfWords = []

    for w in wordNums:
        if w in i:
            indexOfWords.append([[f for f in range(len(i)) if i.startswith(w, f)],w])

    print(indexOfWords)

    for f in range(0, len(i)):
        print(i[f])
        if indexOfWords != []:
            if i[f].isnumeric():
                nums.append(i[f])
            else:
                for word in indexOfWords:
                    if len(word[0]) >= 2:
                        for g in word[0]:
                            if g == f:
                                nums.append(word[1])
                    elif f == word[0][0]:
                        nums.append(word[1])
        else:
            if i[f].isnumeric():
                print("added ", i[f])
                nums.append(i[f])

    print("nums", nums)

    print(i)

    if len(nums) >= 2:
        if nums[0].isnumeric():
            num = nums[0]
        else:
            num = str(wordNums.index(nums[0]) + 1)
        if nums[-1].isnumeric():
            num += nums[-1]
        else:
            num += str(wordNums.index(nums[-1]) + 1)
    elif len(nums) == 1:
        if nums[0].isnumeric():
            num = nums[0]+nums[0]
        else:
            num = str(wordNums.index(nums[0]) + 1)+str(wordNums.index(nums[0]) + 1)
        

    print(num)
    
    if num.isnumeric():
        numbers.append(int(num))

print(sum(numbers))