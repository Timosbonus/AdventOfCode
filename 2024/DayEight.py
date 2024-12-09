from collections import defaultdict
from itertools import permutations

f = open("Input Files/input8.txt")
lines = f.readlines()

def createSatMap(lines):
    return [list(line.strip()) for line in lines]

def findSats(satMap):
    antennas = defaultdict(list)

    for i, row in enumerate(satMap):
        for j, curType in enumerate(row):
            if curType != ".":
                antennas[curType].append((i, j))
    
    return antennas

def firstGoldStar(lines):
    satMap = createSatMap(lines)
    antennas = findSats(satMap)
    
    antinodes = set()

    for coords in antennas.values():
        pairs = list(permutations(coords,2))
        for pair in pairs:
            first,second = pair[0],pair[1]
            anti = [0,0]

            anti[0] = 2 * second[0] - first[0]
            anti[1] = 2 * second[1] - first[1]

            if 0 <= anti[0] < len(satMap) and 0 <= anti[1] < len(satMap[0]):
                antinodes.add(tuple(anti))
        
    return len(antinodes)


def secondGoldStar(lines):
    satMap = createSatMap(lines)
    antennas = findSats(satMap)

    antinodes = set()

    for coords in antennas.values():
        pairs = list(permutations(coords,2))
        for pair in pairs:
            first,second = pair[0],pair[1]

            antinodes.add(tuple(first))
            antinodes.add(tuple(second))

            while True:
                anti = [0,0]

                anti[0] = 2 * second[0] - first[0]
                anti[1] = 2 * second[1] - first[1]

                if 0 <= anti[0] < len(satMap) and 0 <= anti[1] < len(satMap[0]):
                    antinodes.add(tuple(anti))
                else:
                    break

                first, second = second, anti
        
    return len(antinodes)


print("First Gold Star:",firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))