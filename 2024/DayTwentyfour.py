def create_value_map(lines):
    data = {}
    sections = "".join(lines).split("\n\n")
    calculations = []

    for line in sections[0].strip().split("\n"):
        key, value = line.split(": ")
        data[key] = True if value == "1" else False


    for line in sections[1].strip().split("\n"):
        calculation = []
        parts = line.split(" -> ")
        inputs = parts[0].split(" ")
        target = parts[1]
        calculation.extend(inputs)
        calculation.append(target)
        calculations.append(calculation)
        for key in inputs + [target]:
            if key not in data and key != "XOR" and key != "AND" and key != "OR":
                data[key] = -1

    return data, calculations

def check_z_values(value_map):
    for key in value_map:
        if key[0] == "z" and value_map[key] == -1:
            return False
    return True

def perform_calculation(calc, value_map):
    if value_map[calc[0]] == -1 or value_map[calc[2]] == -1:
        return
    if calc[1] == "XOR":
        value_map[calc[3]] = value_map[calc[0]] ^ value_map[calc[2]]
    elif calc[1] == "AND":
        value_map[calc[3]] = value_map[calc[0]] & value_map[calc[2]]
    else:
        value_map[calc[3]] = value_map[calc[0]] | value_map[calc[2]]

def create_z_string(value_map):
    z_keys = {key: value for key, value in value_map.items() if key.startswith("z")}
    sorted_keys = dict(sorted(z_keys.items()))
    s = ""
    for val in sorted_keys.values():
        if val == False:
            s = "0" + s
        else:
            s = "1" + s
    return s

def firstGoldStar(lines):
    value_map, calculations = create_value_map(lines)
    while True:
        for calc in calculations:
            perform_calculation(calc, value_map)
        if check_z_values(value_map):
            break
    s = create_z_string(value_map)
    return int(s, 2)
    

with open("Input Files/input24.txt", "r") as f:
    lines = f.readlines()

print("First Gold Star:", firstGoldStar(lines))


