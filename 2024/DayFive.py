def addToDict(key,val):
    if key not in orderPairs:
        orderPairs[key] = [val]
    else:
        orderPairs[key].append(val)

f = open("Input Files/input5.txt","r")
lines = f.readlines()

orderPairs = dict()
orderCheckList = list()

for line in lines:
    line = line.strip()
    if "|" in line:
        key, val = line.split("|")
        addToDict(key,val)
    elif "," in line:
        orderCheckList.append(line.split(","))

def checkCurrentLine(curLine):
    enc = list()
    length = len(curLine)
    for i in range(length):
        enc.append(curLine[i])
        if (curLine[i] in orderPairs and any(item in orderPairs[curLine[i]] for item in enc)):
            return 0

    return int(curLine[length // 2])

def replaceAndReturn(curLine):
    length = len(curLine)

    for i in range(length - 1):
        index = i
        
        while index >= 0:
            if curLine[index + 1] in orderPairs:
                if curLine[index] in orderPairs[curLine[index + 1]]:
                    curLine[index],curLine[index + 1] = curLine[index + 1],curLine[index]

            index -= 1
    # very baaaad runtime :(

    return int(curLine[length // 2])

def firstGoldStar():
    count = 0

    for curLine in orderCheckList:
        count += checkCurrentLine(curLine)
 
    return count

def secondGoldStar():
    count = 0
    for curLine in orderCheckList:
        if checkCurrentLine(curLine) == 0:
            count += replaceAndReturn(curLine)
    return count


print("First Gold Star:", firstGoldStar())
print("Second Gold Star:", secondGoldStar())


        
