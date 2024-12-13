with open("Input Files/inputTest","r") as f:
    lines = f.readlines()

def createFarmArea(lines):
    return [list(line.strip()) for line in lines]

def checkNotInBounds(i, j, rows, cols):
    return i < 0 or i >= rows or j < 0 or j >= cols

def findRegions(farm, visited, areaCoords, i, j, rows, cols, prevChar):
    if checkNotInBounds(i,j,rows,cols) or (i, j) in visited or not checkNotInBounds(i,j,rows,cols) and farm[i][j] != prevChar:
        return
        
    visited.add((i,j))
    areaCoords.add((i,j))
    for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        findRegions(farm, visited, areaCoords, i + di, j + dj, rows, cols, prevChar)

def checkSurroundings(coord, farm, charToCheck, rows, cols):
    count = 0
    if coord[0] > 0 and farm[coord[0] - 1][coord[1]] != charToCheck or coord[0] == 0: count += 1
    if coord[0] < rows - 1 and farm[coord[0] + 1][coord[1]] != charToCheck or coord[0] == rows - 1: count += 1
    if coord[1] > 0 and farm[coord[0]][coord[1] - 1] != charToCheck or coord[1] == 0: count += 1
    if coord[1] < cols - 1 and farm[coord[0]][coord[1] + 1] != charToCheck or coord[1] == cols - 1: count += 1
    return count

def checkFencesCount(farm, areaCoords, charToCheck, rows, cols):
    count = 0
    for coord in areaCoords:
        count += checkSurroundings(coord, farm, charToCheck, rows, cols)
    return count


def checkSides(farm, areaCoords, charToCheck, rows, cols):
    count = 0
    direction = [0, 1]
    sortedBorders = sorted(areaCoords)
    startPoint, curPlace = [sortedBorders[0][0] - 1, sortedBorders[0][1] - 1, direction[0], direction[1]], [sortedBorders[0][0] - 1 + direction[0], sortedBorders[0][1] - 1 + direction[1]]
    print(curPlace)
    

    return count


def firstGoldStar(lines):
    count = 0
    farm = createFarmArea(lines)
    rows, cols = len(farm), len(farm[0])
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                areaCoords = set()
                findRegions(farm, visited, areaCoords, i, j, rows, cols, farm[i][j])
                perimeter = checkFencesCount(farm, areaCoords, farm[i][j], rows, cols)
                count += len(areaCoords) * perimeter
    
    return count

def secondGoldStar(lines):
    count = 0
    farm = createFarmArea(lines)
    rows, cols = len(farm), len(farm[0])
    visited = set()
    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                areaCoords = set()
                findRegions(farm, visited, areaCoords, i, j, rows, cols, farm[i][j])
                areaCount = len(areaCoords)
                perimeter = checkSides(farm, areaCoords, farm[i][j], rows, cols)
                count += areaCount * perimeter
    
    return count



print("First Gold Star:", firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))



