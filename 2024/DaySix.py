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

def firstGoldStar(pos):
    count = 0
    direction = [-1, 0]

    while True:
        if pos[0] < 0 or pos[0] >= rows - 1 or pos[1] < 0 or pos[1] >= cols - 1:
            break 
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            if direction == [-1, 0]: 
                direction = [0, 1] 
            elif direction == [0, 1]: 
                direction = [1, 0]  
            elif direction == [1, 0]: 
                direction = [0, -1] 
            elif direction == [0, -1]:
                direction = [-1, 0]
        
        pos[0] += direction[0]
        pos[1] += direction[1]

        if field[pos[0]][pos[1]] != "O":
            count += 1
        field[pos[0]][pos[1]] = "O"


    return count


def isReachable(field, pos, target, direction):
    while pos != target:
        # Check bounds and obstacles
        if (pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols or 
                field[pos[0]][pos[1]] == "#"):
            return False
        pos[0] += direction[0]
        pos[1] += direction[1]
    return True

  

def secondGoldStar(pos):


    count = 0
    direction = [-1, 0]  # Initial direction

    rowTurnBook = dict()
    colTurnBook = dict()

    while True:

        # Break if out of bounds
        if pos[0] + direction[0] < 0 or pos[0] + direction[0] >= rows or pos[1] + direction[1] < 0 or pos[1] + direction[1] >= cols:
            break

        # Change direction if hitting a wall
        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":

            # check, if col is in row
            if pos[0] not in rowTurnBook:
                rowTurnBook[pos[0]] = []
            rowTurnBook[pos[0]].append(pos[1])

            if pos[1] not in colTurnBook:
                colTurnBook[pos[1]] = []
            colTurnBook[pos[1]].append(pos[0])

            if direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [1, 0]:
                direction = [0, -1]
            elif direction == [0, -1]:
                direction = [-1, 0]

        # Move and mark position
        pos[0] += direction[0]
        pos[1] += direction[1]
        field[pos[0]][pos[1]] = "O"  # Mark as visited

        if direction == [-1, 0] and pos[0] in rowTurnBook:
            next_bigger = min((value for value in rowTurnBook[pos[0]] if value > pos[1]), default=-1)
            if next_bigger != -1 and isReachable(field, pos.copy(), [pos[0], next_bigger], [0,1]): 
                count+= 1
        if direction == [1, 0] and pos[0] in rowTurnBook:
            next_smaller = max((value for value in rowTurnBook[pos[0]] if value < pos[1]), default=-1)
            if next_smaller != -1 and isReachable(field,pos.copy(), [pos[0], next_smaller], [0,-1]): 
                count+= 1
        if direction == [0, 1] and pos[1] in colTurnBook:
            next_bigger = min((value for value in colTurnBook[pos[1]] if value > pos[0]), default=-1)
            if next_bigger != -1 and isReachable(field, pos.copy(), [next_bigger, pos[1]], [1,0]):
                count += 1
        if direction == [0, -1] and pos[1] in colTurnBook:
            next_smaller = max((value for value in colTurnBook[pos[1]] if value < pos[0]), default=-1)
            if next_smaller != -1 and isReachable(field, pos.copy(), [next_smaller, pos[1]], [-1,0]):
                count += 1
        

    return count

def checkPath(pos, direction):
    encounteredCoords = set()
    encounteredCoords.add(tuple(pos))  # Ensure coordinates are hashable

    while True:
        if tuple(pos) in encounteredCoords:
            return True
        encounteredCoords.add(tuple(pos))

        if direction == [-1, 0]:
            direction = [0, 1]
        elif direction == [0, 1]:
            direction = [1, 0]
        elif direction == [1, 0]:
            direction = [0, -1]
        elif direction == [0, -1]:
            direction = [-1, 0]

        if pos[0] < 0 or pos[0] >= rows or pos[1] < 0 or pos[1] >= cols:
            break  # Out of bounds

        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            if direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [1, 0]:
                direction = [0, -1]
            elif direction == [0, -1]:
                direction = [-1, 0]

        pos[0] += direction[0]
        pos[1] += direction[1]

    return False

def secondBruteForce(pos):
    count = 0
    direction = [-1, 0]

    while True:
        if pos[0] + direction[0] < 0 or pos[0] + direction[0] >= rows or pos[1] + direction[1] < 0 or pos[1] + direction[1] >= cols:
            break

        if checkPath(pos.copy(), direction.copy()):
            count += 1

        if field[pos[0] + direction[0]][pos[1] + direction[1]] == "#":
            if direction == [-1, 0]:
                direction = [0, 1]
            elif direction == [0, 1]:
                direction = [1, 0]
            elif direction == [1, 0]:
                direction = [0, -1]
            elif direction == [0, -1]:
                direction = [-1, 0]

        pos[0] += direction[0]
        pos[1] += direction[1]

    return count

#print("First Gold Star:", firstGoldStar(pos))
print("Second Gold Star:", secondBruteForce(pos))



