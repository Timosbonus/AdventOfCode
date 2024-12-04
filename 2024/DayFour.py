f = open("Input Files/input4.txt","r")
lines = f.readlines()

field = []

for line in lines:
    field.append(list(line))

maxRow = len(field)
maxCol = len(field[0])


def checkTop(row,col):
    if row < 3:
        return 0
    
    if field[row - 1][col] == "M" and field[row - 2][col] == "A" and field[row - 3][col] == "S":
        return 1
    return 0

def checkDown(row,col):
    if maxRow - row < 4:
        return 0
    
    if field[row + 1][col] == "M" and field[row + 2][col] == "A" and field[row + 3][col] == "S":
        return 1
    return 0

def checkLeft(row,col):
    if col < 3:
        return 0
    
    if field[row][col - 1] == "M" and field[row][col - 2] == "A" and field[row][col - 3] == "S":
        return 1
    return 0

def checkRight(row,col):
    if maxCol - col < 4:
        return 0
    
    if field[row][col + 1] == "M" and field[row][col + 2] == "A" and field[row][col + 3] == "S":
        return 1
    return 0

def checkTopLeft(row,col):
    if row < 3 or col < 3:
        return 0
    
    if field[row - 1][col - 1] == "M" and field[row - 2][col - 2] == "A" and field[row - 3][col - 3] == "S":
        return 1
    return 0

def checkTopRight(row,col):
    if row < 3 or maxCol - col < 4:
        return 0
    
    if field[row - 1][col + 1] == "M" and field[row - 2][col + 2] == "A" and field[row - 3][col + 3] == "S":
        return 1
    return 0

def checkDownLeft(row,col):
    if maxRow - row < 4 or col < 3:
        return 0
    
    if field[row + 1][col - 1] == "M" and field[row + 2][col - 2] == "A" and field[row + 3][col - 3] == "S":
        return 1
    return 0

def checkDownRight(row,col):
    if maxRow - row < 4 or maxCol - col < 4:
        return 0
    
    if field[row + 1][col + 1] == "M" and field[row + 2][col + 2] == "A" and field[row + 3][col + 3] == "S":
        return 1
    return 0


def firstGoldStar():
    count = 0

    for row in range(maxRow):
        for col in range(maxCol):
            if field[row][col] == "X":
                count += checkTop(row,col)
                count += checkDown(row,col)
                count += checkLeft(row,col)
                count += checkRight(row,col)
                count += checkTopLeft(row,col)
                count += checkTopRight(row,col)
                count += checkDownLeft(row,col)
                count += checkDownRight(row,col)
    
    return count



def checkTopLeftDownRight(row,col):
    return (field[row - 1][col - 1] == "M" and field[row + 1][col + 1] == "S") or (field[row - 1][col - 1] == "S" and field[row + 1][col + 1] == "M")

def checkTopRightDownLeft(row,col):
    return (field[row - 1][col + 1] == "M" and field[row + 1][col - 1] == "S") or (field[row - 1][col + 1] == "S" and field[row + 1][col - 1] == "M")


def checkMas(row,col):
    if row == 0 or col == 0 or maxRow - row < 2 or maxCol - col < 2:
        return 0
    
    if checkTopLeftDownRight(row,col) and checkTopRightDownLeft(row,col):
        return 1
    return 0
    
    

def secondGoldStar():
    count = 0
    for row in range(maxRow):
        for col in range(maxCol):
            if field[row][col] == "A":
                count += checkMas(row,col)

    return count

        

print("First Gold Star:",firstGoldStar())
print("Second Gold Star:",secondGoldStar())