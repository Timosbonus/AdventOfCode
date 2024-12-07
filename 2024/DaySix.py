import copy

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
        return [0, 1] 
    elif direction == [0, 1]: 
        return [1, 0]  
    elif direction == [1, 0]: 
        return [0, -1] 
    elif direction == [0, -1]:
        return [-1, 0]

def is_out_of_bounds(pos, rows, cols):
    return not (0 <= pos[0] < rows and 0 <= pos[1] < cols)

def firstGoldStar(pos,field):
    count = 0
    direction = [-1, 0]

    while True:
        if pos[0] + direction[0] < 0 or pos[0] + direction[0] >= rows or pos[1] + direction[1] < 0 or pos[1] + direction[1] >= cols:
            break 
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = turnRight(direction)
        
        pos[0] += direction[0]
        pos[1] += direction[1]

        if field[pos[0]][pos[1]] != "O":
            count += 1
        field[pos[0]][pos[1]] = "O"


    return count + 1

def secondGoldStar(pos,field):
    count = 0

    posObstacles = set()

    # walk every position
    direction = [-1, 0]

    while True:
        if is_out_of_bounds([pos[0] + direction[0], pos[1] + direction[1]], rows, cols):
            return False

        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = turnRight(direction)
        
        posToCheck = pos.copy()
        posToCheck[0] += direction[0]
        posToCheck[1] += direction[1]       

        if (0 <= posToCheck[0] < rows and 0 <= posToCheck[1] < cols) and field[posToCheck[0]][posToCheck[1]] == ".":
            changedField = copy.deepcopy(field)
            changedField[posToCheck[0]][posToCheck[1]] = "#"

            # Check if this path leads to a loop
            if checkPath(pos.copy(), direction.copy(), changedField):
                posObstacles.add(tuple(posToCheck))
                count += 1
        
        pos[0] += direction[0]
        pos[1] += direction[1]
        
    return count


def checkPath(pos, direction, field):
    # change direction
    direction = turnRight(direction)

    # save positions in a set
    encounteredPositions = set()

    # walk steps like in firstGoldStar
    while True:
        if is_out_of_bounds([pos[0] + direction[0], pos[1] + direction[1]], rows, cols):
            return False
         
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            direction = turnRight(direction)

        
        pos[0] += direction[0]
        pos[1] += direction[1]

        # check if new position already in set
        
        pos_tuple = (pos[0], pos[1], direction[0], direction[1])
        if pos_tuple in encounteredPositions:
            return True

        encounteredPositions.add(pos_tuple)
        
    


print("First Gold Star:", firstGoldStar(pos.copy(), field.copy()))
print("Second Gold Star:", secondGoldStar(pos.copy(), field.copy()))




