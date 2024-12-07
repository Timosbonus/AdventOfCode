f = open("Input Files/input6.txt", "r")
lines = f.readlines()

field = list()

for line in lines:
    stripped = line.strip()
    field.append(list(stripped))

pos = [0, 0]

rows = len(field)
cols = len(field[0])

for i in range(rows):
    for j in range(cols):
        if field[i][j] == "^":
            pos = [i, j]

def turnRight(direction):
    if direction == [-1, 0]: 
        direction = [0, 1] 
    elif direction == [0, 1]: 
        direction = [1, 0]  
    elif direction == [1, 0]: 
        direction = [0, -1] 
    elif direction == [0, -1]:
        direction = [-1, 0]

    return direction

def firstGoldStar(pos):
    count = 0
    direction = [-1, 0]

    while True:
        if pos[0] < 0 or pos[0] >= rows - 1 or pos[1] < 0 or pos[1] >= cols - 1:
            break 
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = turnRight(direction)
        
        pos[0] += direction[0]
        pos[1] += direction[1]

        if field[pos[0]][pos[1]] != "O":
            count += 1
        field[pos[0]][pos[1]] = "O"


    return count

def secondGoldStar(pos):
    count = 0
    obstacleRowMap = dict()
    obstacleColMap = dict()

    posObstacles = set()


    # walk every position
    direction = [-1, 0]

    while True:
        if pos[0] < 0 or pos[0] >= rows - 1 or pos[1] < 0 or pos[1] >= cols - 1:
            break 
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = turnRight(direction)
        
        pos[0] += direction[0]
        pos[1] += direction[1]

        if checkPath(pos.copy(), direction.copy()) and tuple(pos) not in posObstacles:
            posObstacles.add(tuple(pos))
            count += 1

    # check depending on position and direction, if obstacle is in row or col


    # if true -> checkPath(pos, direction)


    # if checkPath returns True, add count


    return count


def checkPath(pos, direction):
    
    # change direction
    direction = turnRight(direction)

    # save positions in a set

    encounteredPositions = set()

    # walk steps like in firstGoldStar

    while True:
        if pos[0] < 0 or pos[0] >= rows - 1 or pos[1] < 0 or pos[1] >= cols - 1:
            return False
         
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = turnRight(direction)

        
        pos[0] += direction[0]
        pos[1] += direction[1]

        # check if new position already in set
        if tuple(pos) in encounteredPositions:
            return True
        
        encounteredPositions.add(tuple(pos))



print("First Gold Star:", firstGoldStar(pos.copy()))
print("Second Gold Star:", secondGoldStar(pos.copy()))




