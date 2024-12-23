import itertools

def create_map(lines):
    con_dict = dict()
    unique_vals = set()
    for line in lines:
        con = line.strip().split("-")
        if con[0] not in con_dict:
            con_dict[con[0]] = set()
        if con[1] not in con_dict:
            con_dict[con[1]] = set()
        con_dict[con[0]].add(con[1])
        con_dict[con[1]].add(con[0])
        unique_vals.add(con[0])
        unique_vals.add(con[1])
        
    return con_dict, unique_vals
        
def find_connected_pairs(possible_pairs, connection_map):
    correct_pairs = set()
    for pair in possible_pairs:
        if (pair[0] in connection_map[pair[1]] and pair[0] in connection_map[pair[2]] and pair[1] in connection_map[pair[2]]):
            correct_pairs.add(pair)
    return correct_pairs


def getMapCount(connection_map, unique_vals):
    pairs = itertools.combinations(unique_vals, 3)
    possible_pairs = [comb for comb in sorted(pairs) if any("t" in val[0] for val in comb)]
    return len(find_connected_pairs(possible_pairs, connection_map))


def firstGoldStar(lines):
    connection_map, unique_vals = create_map(lines)
    return getMapCount(connection_map, unique_vals)

with open("Input Files/input23.txt","r") as f:
    lines = f.readlines()
    

print("First Gold Star:", firstGoldStar(lines))