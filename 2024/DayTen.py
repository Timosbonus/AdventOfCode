f = open("Input Files/input10.txt", "r")
lines = f.readlines()

def create2dArr(lines):
    return [[int(char) for char in line.strip()] for line in lines]

def findTrails(i,j,rows,cols, heightMap, visited):
    if heightMap[i][j] == 9 and tuple([i,j]) not in visited:
        visited.add(tuple[i,j])
        return 1
    
    if i - 1 >= 0 and heightMap[i][j] + 1 == heightMap[i-1][j]: findTrails(i-1,j,rows,cols,heightMap,visited)
    if i + 1 < rows and heightMap[i][j] + 1 == heightMap[i+1][j]: findTrails(i+1,j,rows,cols,heightMap,visited)
    if j - 1 >= 0 and heightMap[i][j] + 1 == heightMap[i][j-1]: findTrails(i,j-1,rows,cols,heightMap,visited)
    if j + 1 < cols and heightMap[i][j] + 1 == heightMap[i][j+1]: findTrails(i,j+1,rows,cols,heightMap,visited)

    return len(visited)

def findDistinctTrails(i,j,rows,cols, heightMap):
    if heightMap[i][j] == 9 and tuple([i,j]):
        return 1
    count = 0
    if i - 1 >= 0 and heightMap[i][j] + 1 == heightMap[i-1][j]: count += findDistinctTrails(i-1,j,rows,cols,heightMap)
    if i + 1 < rows and heightMap[i][j] + 1 == heightMap[i+1][j]: count += findDistinctTrails(i+1,j,rows,cols,heightMap)
    if j - 1 >= 0 and heightMap[i][j] + 1 == heightMap[i][j-1]: count += findDistinctTrails(i,j-1,rows,cols,heightMap)
    if j + 1 < cols and heightMap[i][j] + 1 == heightMap[i][j+1]: count += findDistinctTrails(i,j+1,rows,cols,heightMap)

    return count


def firstGoldStar(lines):
    count = 0
    heightMap = create2dArr(lines)
    rows, cols = len(heightMap), len(heightMap[0])
    for i in range(rows):
        for j in range(cols):
            if heightMap[i][j] == 0:
                visited = set()
                count += findTrails(i,j,rows, cols, heightMap, visited)
    return count

def secondGoldStar(lines):
    count = 0
    heightMap = create2dArr(lines)
    rows, cols = len(heightMap), len(heightMap[0])
    for i in range(rows):
        for j in range(cols):
            if heightMap[i][j] == 0:
                count += findDistinctTrails(i,j,rows, cols, heightMap)
    return count
    

print("First Gold Star:", firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))