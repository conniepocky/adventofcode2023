import re

with open ("practise.txt", "r") as f:
    rows = f.read().splitlines()
    
symbols = ["$", "#", "@", "%", "&", "*", "!", "?", "~", "^", "+", "-", "_", "=", "<", ">", ":", ";", "|", "/"]

#print(rows)

ans = 0

def findNearbySymbol(index, rowIndex):
    #print(index, rowIndex)

    indLength = len(rows[rowIndex])-1
    startInd = index[0]
    if index[0] != 0 and index[0] >= 2:
        startInd -= 1

    endInd = index[1]
    if index[1] != indLength and index[1] <= indLength-2:
        endInd += 2

    for s in symbols:
        if rowIndex == 0:
            if s in rows[rowIndex+1][startInd:endInd]:
                return True
        elif rowIndex == len(rows)-1:
            if s in rows[rowIndex-1][startInd:endInd]:
                return True
        else:
            if s in rows[rowIndex+1][startInd:endInd] or s in rows[rowIndex-1][startInd:endInd] or s in rows[rowIndex][startInd:endInd]:
                return True

for rowIndex, row in enumerate(rows):
    temp = re.findall(r'\d+|\D+', row)
    currentIndex = 0
    for i in temp:
        index = [currentIndex, currentIndex+len(i)-1]
        currentIndex += len(i)
        if i.isdigit():
            #print(i)
            if findNearbySymbol(index, rowIndex):
                ans += int(i)
                #print(i, " is part number")
    
print(ans)