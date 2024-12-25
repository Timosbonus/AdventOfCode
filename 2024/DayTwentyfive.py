def create_key_heights(arr_rep, key):
    height_map = []
    for col in range(5):
        for height in range(len(arr_rep)):
            if key and arr_rep[height][col] == "#":
                height_map.append(6 - height)
                break
            elif not key and arr_rep[height][col] == ".":
                height_map.append(height - 1)
                break
    return height_map

def read_input(lines):
    structs = []
    current = []
    for line in lines:
        if line == "\n":
            structs.append(current)
            current = []
        else:
            current.append(list(line.strip()))
    return structs


def firstGoldStar(lines):
    matches = 0
    schematics = read_input(lines)
    key_heights, hole_heights = [],[]
    for current in schematics:
        if "." in current[0]:
            key_heights.append(create_key_heights(current, True))
        else:
            hole_heights.append(create_key_heights(current, False))

    for key in key_heights:
        for hole in hole_heights:
            overlap = False
            for i in range(len(key)):
                if key[i] + hole[i] > 5:
                    overlap = True
                    break
            if not overlap:
                matches += 1

    return matches

with open("Input Files/input25.txt","r") as f:
    lines = f.readlines()

print("First Gold Star:", firstGoldStar(lines))

