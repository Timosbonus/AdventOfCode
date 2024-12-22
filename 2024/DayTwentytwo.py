def evolve_numb(numb):
    copy = numb * 64
    numb = prune(mix(copy, numb))
    two = numb // 32
    numb = prune(mix(numb, two))
    three = numb * 2048
    numb = prune(mix(numb, three))
    return numb


def prune(numb):
    return numb % 16777216

def mix(num_1,num_2):
    return num_1 ^ num_2

with open("Input Files/input22.txt","r") as f:
    lines = f.readlines()

def firstGoldStar(lines):
    count = 0
    for line in lines:
        numb = int(line.strip())
        for _ in range(2000):
            numb = evolve_numb(numb)
        count += numb
    return count

print("First Gold Star:", firstGoldStar(lines))