f = open("Input Files/input9.txt", "r")
line = f.readline()

def addToList(char, times, s):
    for _ in range(times):
        s.append(char)
    return s

def processLine(line):
    s = list()
    for i in range(len(line)):
        if line[i].isdigit() == False: 
            continue
        if i % 2 == 0:
            s = addToList(str(i // 2), int(line[i]), s)
        else:
            s = addToList(".", int(line[i]), s)
    return s

def removeDots(s):
    lastIndex = len(s) - 1
    firstIndex = 0
    while firstIndex <= lastIndex:
        while firstIndex <= lastIndex and s[lastIndex] == ".":
            lastIndex -= 1
        
        while firstIndex <= lastIndex and s[firstIndex] != ".":
            firstIndex += 1

        if firstIndex <= lastIndex:
            s[firstIndex],s[lastIndex] = s[lastIndex], s[firstIndex]
    
    return s

def getBlockSize(s, lastIndex):
    currentChar = s[lastIndex]
    size = 0
    while lastIndex >= 0 and s[lastIndex] == currentChar:
        lastIndex -= 1
        size += 1
    return size

def findFreeSpace(size, lastIndex, s):
    for index in range(lastIndex - size):
        subarray = s[index:index + size]
        if all(char == "." for char in subarray):
            return index + size - 1
    return -1
        
    
def move(newLocation, lastIndex, size, s):
    for i in range(size):
        s[newLocation - i], s[lastIndex - i] = s[lastIndex - i], s[newLocation - i]
    return s


def removeDotsTwo(s):
    # find last block
    lastIndex = len(s) - 1
    while lastIndex >= 0:
        if s[lastIndex] != ".":
            size = getBlockSize(s, lastIndex)
            newLocation = findFreeSpace(size, lastIndex, s)

            if newLocation != -1:
                s = move(newLocation, lastIndex, size, s)
            else:
                lastIndex -= size - 1
        lastIndex -= 1
    
    return s

def filesystemChecksum(s):
    count = 0
    for i in range(len(s)):
        if s[i] == ".": continue
        count += i * int(s[i])
    return count



def firstGoldStar(line):
    fileFreeSpace = processLine(line)
    removedDots = removeDots(fileFreeSpace)
    return filesystemChecksum(removedDots)

def secondGoldStar(line):
    fileFreeSpace = processLine(line)
    removeDots = removeDotsTwo(fileFreeSpace)
    return filesystemChecksum(removeDots)


print("First Gold Star:", firstGoldStar(line))
print("Second Gold Star:", secondGoldStar(line))