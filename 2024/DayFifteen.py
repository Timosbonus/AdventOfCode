with open("Input Files/inputTest","r") as f:
    lines = f.readlines()

def createInputFiles(lines):
    warehouse_map, instructions = [], ""
    for line in lines:
        if any(char in line for char in "#.@O"):
            warehouse_map.append(list(line.strip()))
        elif any(char in line for char in "^<>v"):
            instructions += line.strip()

    return warehouse_map, instructions

def getRobotPosition(warehouse_map):
    for i in range(len(warehouse_map)):
        for j in range(len(warehouse_map[0])):
            if warehouse_map[i][j] == "@":
                return [i,j]
            
def printWarehouseMap(warehouse_map):
    for row in warehouse_map:
        print("".join(row))

def doubleMap(small_map):
    warehouse_map = []
    for row in small_map:
        newRow = []
        for char in row:
            if char == "#":
                newRow.extend(["#", "#"])
            elif char == "O":
                newRow.extend(["[", "]"])
            elif char == ".":
                newRow.extend([".", "."])
            elif char == "@":
                newRow.extend(["@", "."])
        warehouse_map.append(newRow)

    return warehouse_map

def checkAndPerformMove(robot, warehouse_map, direction):
    steps = robot.copy()
    while True:
        steps[0] += direction[0]
        steps[1] += direction[1]
        if warehouse_map[steps[0]][steps[1]] == "#": 
            return robot
        elif warehouse_map[steps[0]][steps[1]] == ".":
            warehouse_map[steps[0]][steps[1]] = "O"
            warehouse_map[robot[0]][robot[1]] = "."
            robot[0], robot[1] = robot[0] + direction[0], robot[1] + direction[1]
            warehouse_map[robot[0]][robot[1]] = "@"
            return robot
        
def checkAndPerformMoveTwo(robot, warehouse_map, direction):
    steps = robot.copy()
    if direction[0] == 0: return checkAndPerformMove(robot, warehouse_map, direction)
    while True:
        steps[0] += direction[0]
        steps[1] += direction[1]
        if warehouse_map[steps[0]][steps[1]] == "#":
            return robot
        ## always need to increase the size 
        

        
def getDirection(ins):
    direction = [0,0]
    if ins == "^":
        direction = [-1 , 0]
    elif ins == "v":
        direction = [1 , 0]
    elif ins == "<":
        direction = [0, -1]
    elif ins == ">":
        direction = [0 , 1]
    return direction

def calculatePositions(warehouse_map):
    count = 0
    for i in range(len(warehouse_map)):
        for j in range (len(warehouse_map[0])):
            if warehouse_map[i][j] == "O" or warehouse_map[i][j] == "[":
                count += 100 * i + j
    return count


def firstGoldStar(lines):
    warehouse_map, instructions = createInputFiles(lines)
    robot = getRobotPosition(warehouse_map)

    for ins in instructions:
        direction = getDirection(ins)
        if direction == [0,0]: continue
        robot = checkAndPerformMove(robot, warehouse_map, direction)
    
    return calculatePositions(warehouse_map)

def secondGoldStar(lines):
    small_map, instructions = createInputFiles(lines)
    warehouse_map = doubleMap(small_map)
    robot = getRobotPosition(warehouse_map)

    for ins in instructions:
        direction = getDirection(ins)
        if direction == [0,0]: continue
        robot = checkAndPerformMoveTwo(robot, warehouse_map, direction)

    return calculatePositions(warehouse_map)

    


print("First Gold Star:" , firstGoldStar(lines))
print("Second Gold Star:" , secondGoldStar(lines))
