f = open("Input Files/input6.txt", "r")
lines = f.readlines()

def changeDirection(direction):
    if direction == [-1,0]:
        return [0,1]
    elif direction == [0,1]:
        return [1,0]
    elif direction == [1,0]:
        return [0,-1]
    else:
        return [-1,0]

def createMap(lines):
    return [list(line.strip()) for line in lines]

def findStart(map):
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "^": return i, j

def checkBounds(pos,rows,cols):
    if 0 <= pos[0] < rows and 0 <= pos[1] < cols:
        return True
    return False

def checkPath(currentPos, guardMap, direction, rows, cols, startPos):
    positionToCheck = [currentPos[0] + direction[0], currentPos[1] + direction[1]]
    if checkBounds(positionToCheck, rows, cols) == False or guardMap[positionToCheck[0]][positionToCheck[1]] != ".":
        return False
    guardMap[positionToCheck[0]][positionToCheck[1]] = "#"
    direction = changeDirection(direction)
    checkForLoop = set()
    checkForLoop.add(tuple([currentPos[0],currentPos[1], direction[0], direction[1]]))

    #while checkBounds(currentPos,rows,cols):



    guardMap[positionToCheck[0]][positionToCheck[1]] = "."



def secondGoldStar(lines):
    count = 0

    guardMap = createMap(lines)
    startPos = findStart(guardMap)

    rows = len(guardMap)
    cols = len(guardMap[0])

    currentPos = [startPos[0],startPos[1]]
    direction = [-1,0]

    while checkBounds(currentPos,rows, cols):
        positionToCheck = [currentPos[0] + direction[0], currentPos[1] + direction[1]]
        if checkBounds(positionToCheck, rows, cols) == False: break





        if checkPath(currentPos, guardMap, direction, rows, cols, startPos): count += 1



print("Second Gold Star:", secondGoldStar(lines))


