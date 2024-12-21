with open("Input Files/inputTest","r") as f:
    lines = f.readlines()

def getNumericCoord(char):
    coords = {
        '1': [2, 0], '2': [2, 1], '3': [2, 2],
        '4': [1, 0], '5': [1, 1], '6': [1, 2],
        '7': [0, 0], '8': [0, 1], '9': [0, 2],
        '0': [3, 1], "A": [3, 2]
    }
    return coords[char]

def getMovementCoord(sign):
    coords = {
        "<": [1, 0], ">": [1, 2], "^": [0, 1],
        "v": [1, 1], "A": [0, 2]
    }
    return coords[sign]
    
    
def translateFromNumeric(line):
    # if dir down -> horizontal first, if up, vertical first up
    instructions = ""
    cur_pos = getNumericCoord("A")
    for char in line:
        num_pos = getNumericCoord(char)
        diff = [num_pos[0] - cur_pos[0], num_pos[1] - cur_pos[1]]
        horizontal_dir = "<" if diff[1] < 0 else ">"
        diff[1] = abs(diff[1])
        if diff[0] > 0:
            instructions += diff[1] * horizontal_dir + diff[0] * "v"
        else:
            instructions += abs(diff[0]) * "^" + diff[1] * horizontal_dir
        instructions += "A"
        cur_pos = num_pos

    print(instructions)

    return instructions


    
def translateFromDirectional(instructions):
    ins = ""
    cur_pos = getMovementCoord("A")
    for char in instructions:
        ins_pos = getMovementCoord(char)
        diff = [ins_pos[0] - cur_pos[0], ins_pos[1] - cur_pos[1]]
        horizontal_dir = "<" if diff[1] < 0 else ">"
        diff[1] = abs(diff[1])
        if diff[0] > 0:
            ins += diff[0] * "v" + diff[1] * horizontal_dir
        else:
            ins += diff[1] * horizontal_dir + abs(diff[0]) * "^"
        ins += "A"
        cur_pos = ins_pos
    print(ins)
    return ins

    

def firstGoldStar(lines):
    count = 0
    for line in lines:
        print(line.strip())
        instruction_one = translateFromNumeric(line.strip())
        instruction = translateFromDirectional(translateFromDirectional(instruction_one))
        print("Len:", len(instruction))
        count += int(line[:3]) * len(instruction)

    return count

print("First Gold Star:", firstGoldStar(lines))