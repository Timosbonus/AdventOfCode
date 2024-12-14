import math

with open("Input Files/input14.txt","r") as f:
    lines = f.readlines()

def robotMovements(line):
    parts = line.strip().split(" ")
    
    p = parts[0].split("=")[1].strip("()").split(",")
    p = tuple(map(int, p))
    
    v = parts[1].split("=")[1].strip("()").split(",")
    v = tuple(map(int, v)) 

    return p, v

def calculatePosition(p, v, width, height, secs):
    p = list(p)
    p[0] = (p[0] + v[0] * secs) % width
    p[1] = (p[1] + v[1] * secs) % height

    return tuple(p)

def addToQuaderCount(pos, quadrantCount, width, height):
    widthMid, heightMid = width // 2, height // 2
    num = -1
    if pos[0] < widthMid and pos[1] < heightMid:
        num = 0
    elif pos [0] > widthMid and pos[1] < heightMid:
        num = 1
    elif pos[0] < widthMid and pos[1] > heightMid:
        num = 2
    elif pos[0] > widthMid and pos[1] > heightMid:
        num = 3
    if num != -1: 
        quadrantCount[num] += 1

def firstGoldStar(lines):
    quadrantCount = [0,0,0,0]
    width, height = 101, 103
    for line in lines:
        p, v = robotMovements(line)
        newPos = calculatePosition(p, v, width, height, 100)
        addToQuaderCount(newPos, quadrantCount, width, height)
    
    return math.prod(quadrantCount)

def secondGoldStar(lines):
    width, height = 101, 103
    robot_list = [robotMovements(line) for line in lines]
    index = 0
    while True:
        
        roboPlace = set()
        found = True
        for idx, robot in enumerate(robot_list):
            position, velocity = robot
            new_position = calculatePosition(position, velocity, width, height, 1)
            robot_list[idx] = (new_position, velocity)
            if new_position in roboPlace:
                found = False
                break
            roboPlace.add(new_position)
        if found:
            return index
        index += 1
    

        
        

print("First Gold Star:", firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))
