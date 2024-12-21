with open("Input Files/input20.txt","r") as f:
    lines = f.readlines()

def createRaceTrack(lines):
    track = list()
    for line in lines:
        track.append(list(line.strip()))
    return track

def findPosition(sign, track):
    for i in range(len(track)):
        for j in range(len(track[0])):
            if track[i][j] == sign:
                track[i][j] = "0"
                return (i, j)

def checkBounds(pos, track):
    rows = len(track)
    cols = len(track[0])
    if int(pos[0]) < 0 or int(pos[0]) >= rows or int(pos[1]) < 0 or int(pos[1]) >= cols:
        return False
    return True

def numerateTrack(start, track):
    count = 1
    pos = [start[0], start[1]]
    positions = set()
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    while track[pos[0]][pos[1]] != "E":
        for dx, dy in directions:
            if track[pos[0] + dx][pos[1] + dy] == "." or track[pos[0] + dx][pos[1] + dy] == "E":
                positions.add(tuple(pos))
                pos[0] += dx
                pos[1] += dy
                sign = track[pos[0]][pos[1]]
                track[pos[0]][pos[1]] = str(count)
                if sign == "E":
                    positions.add(tuple(pos))
                    return positions
                count += 1
                break

def printTrack(track):
    for row in track:
        print(row)

def checkForShortcuts(track, positions, save_amount):
    count = 0
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    for pos in positions:
        for dx, dy in directions:
            shortcut_pos = [pos[0] + 2 * dx, pos[1] + 2 * dy]
            if (track[pos[0] + dx][pos[1] + dy] == "#" and checkBounds(shortcut_pos, track) 
                and track[shortcut_pos[0]][shortcut_pos[1]] != "#"):
                if int(track[shortcut_pos[0]][shortcut_pos[1]]) - int(track[pos[0]][pos[1]]) > save_amount:
                    count += 1
                
    return count

def firstGoldStar(lines):
    track = createRaceTrack(lines)
    start = findPosition("S", track)
    positions = numerateTrack(start, track)
    return checkForShortcuts(track, positions, 100)

print("First Gold Star:", firstGoldStar(lines))