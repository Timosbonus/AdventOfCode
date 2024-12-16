with open("Input Files/input16.txt","r") as f:
    lines = f.readlines()

def createMaze(lines):
    return [list(line.strip()) for line in lines]

class QItem:
    def __init__(self, row, col, dist, direction):
        self.row = row
        self.col = col
        self.dist = dist
        self.direction = direction

    def __repr__(self):
        return f"QItem({self.row}, {self.col}, {self.dist})"

# direction 0 right, 1 up, 2 left, 3 down
def minDistance(grid):
    source = QItem(0, 0, 0, 0)

    # Create a distance array initialized to a very high value
    distances = [[float('inf') for _ in range(len(grid[0]))]
                 for _ in range(len(grid))]
 
    # Find the starting point 'S'
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'S':
                source.row = row
                source.col = col
                distances[row][col] = 0  # Distance to the start is 0

    queue = [source]
    lowest = float('inf')
    while queue:
        source = queue.pop(0)
        current_distance = distances[source.row][source.col]

        # Destination found
        if grid[source.row][source.col] == 'E':
            lowest = min(source.dist, lowest)

        # Explore neighbors
        for dx, dy, direction in [(-1, 0, 1), (1, 0, 3), (0, -1, 2), (0, 1, 0)]:
            new_row, new_col = source.row + dx, source.col + dy
            if isValid(new_row, new_col, grid):
                # Calculate the new distance
                valToAdd = 1
                if source.direction != direction:
                    valToAdd += 1000
                new_distance = current_distance + valToAdd

                # Update the distance if the new path is shorter
                if new_distance < distances[new_row][new_col]:
                    distances[new_row][new_col] = new_distance
                    queue.append(QItem(new_row, new_col, new_distance, direction))
 
    return -1 if lowest == float('inf') else lowest

def isValid(x, y, grid):
    return (0 <= x < len(grid)) and (0 <= y < len(grid[0])) and (grid[x][y] != '#')

# doesnt correctly handle the first turn, so result += 1000 :D
def firstGoldStar(lines):
    maze = createMaze(lines)
    return minDistance(maze)

print("First Gold Star:", firstGoldStar(lines))

