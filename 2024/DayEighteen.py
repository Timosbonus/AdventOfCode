from collections import deque

def createGrid(size):
    grid = list()
    for _ in range(size):
        row = list()
        for _ in range(size):
            row.append(".")
        grid.append(row)
    return grid

def placeObstacles(lines,visited,grid,max_bytes):
    bytes = 0
    for line in lines:
        coords = line.strip().split(",")
        grid[int(coords[1])][int(coords[0])] = "#"
        visited.add((int(coords[1]), int(coords[0])))
        bytes += 1
        if bytes == max_bytes: break

def printGrid(grid):
    for i in range(len(grid)):
        print(grid[i])

def bfs(visited, grid):
    start = (0,0)
    size = len(grid)
    end = (size - 1, size - 1)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start, 0)])

    while queue:
        (x, y), distance = queue.popleft()

        if (x, y) == end: return distance

        visited.add((x, y))

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and grid[nx][ny] != "#":
                queue.append(((nx,ny), distance + 1))
                visited.add((nx, ny))

    return -1

def firstGoldStar(lines):
    grid = createGrid(71)
    visited = set()
    placeObstacles(lines, visited, grid, 1024)
    return bfs(visited, grid)

with open("Input Files/input18.txt","r") as f:
    lines = f.readlines()

print("First Gold Star:", firstGoldStar(lines))