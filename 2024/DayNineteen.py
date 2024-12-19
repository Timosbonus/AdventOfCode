import re

with open("Input Files/input19.txt","r") as f:
    lines = f.readlines()

def createKnownPatterns(lines):
    patterns = list()
    for line in lines:
        if "," not in line: continue
        line = line.strip()
        patterns.extend(line.split(", "))
    patterns.sort(reverse=True, key=len)
    return patterns

def createDesigns(lines):
    designs = list()
    for line in lines:
        if "," in line or line == "\n": continue
        designs.append(line.strip())
    return designs

# help from LLM to come up with this solution
def checkValid(design, patterns):
    n = len(design)
    dp = [0] * (n + 1)
    dp[0] = True

    for i in range(n):
        if dp[i]:
            for pattern in patterns:
                pat_len = len(pattern)
                if i + pat_len <= n and design[i:i + pat_len] == pattern:
                    dp[i + pat_len] = True

    return dp[n]


def firstGoldStar(lines):
    patterns = createKnownPatterns(lines)
    designs = createDesigns(lines)
    count = 0
    for design in designs:
        if checkValid(design, patterns): count += 1
    return count

print("First Gold Star:", firstGoldStar(lines))