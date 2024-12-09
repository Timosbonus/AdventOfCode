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

def getHoles(s):
    holes = {}
    currentHoleStart = None
    currentHoleSize = 0
    for i in range(len(s)):
        if s[i] == ".":
            if currentHoleStart is None:
                currentHoleStart = i
                currentHoleSize = 1
            else:
                currentHoleSize += 1
        else:
            if currentHoleStart is not None:
                holes[currentHoleStart] = currentHoleSize
                currentHoleStart = None
                currentHoleSize = 0
    if currentHoleStart is not None:
        holes[currentHoleStart] = currentHoleSize
    return holes

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

def findFreeSpace(size, holes, lastIndex):
    sorted_holes = sorted(holes.items())
    for start, hole_size in sorted_holes:
        if start >= lastIndex: break
        if hole_size >= size:
            return start, hole_size
    return None, None
        
    
def move(newLocation, lastIndex, size, s):
    for i in range(size):
        s[newLocation + i], s[lastIndex - i] = s[lastIndex - i], s[newLocation + i]
    return s


def removeDotsTwo(s):
    holes = getHoles(s)
    lastIndex = len(s) - 1
    moved = set()
    
    while lastIndex >= 0:
        if s[lastIndex] != "." and s[lastIndex] not in moved:
            moved.add(s[lastIndex])
            size = getBlockSize(s, lastIndex)
            newLocation, hole_size = findFreeSpace(size, holes, lastIndex)            

            if newLocation is not None:
                s = move(newLocation, lastIndex, size, s)
               
                
                del holes[newLocation]
                if size != hole_size:
                    holes[newLocation + size] = hole_size - size


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