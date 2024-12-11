from collections import Counter

# Parse input and initialize counts
def createCounter(line):
    return Counter(int(num) for num in line.split(" "))

def workCurNumb(num):
    if num == 0: 
        return [1]
    sNum = str(num)
    len_num = len(sNum)
    if len_num % 2 == 0:
        mid = len_num // 2
        return [int(sNum[:mid]), int(sNum[mid:])]
    return [num * 2024]

def processCounts(counter, times):
    for _ in range(times):
        new_counter = Counter()
        for num, count in counter.items():
            new_vals = workCurNumb(num)
            for val in new_vals:
                new_counter[val] += count
        counter = new_counter
    return sum(counter.values())

def firstGoldStar(line, times):
    counter = createCounter(line)
    return processCounts(counter, times)

# Input
with open("Input Files/input11.txt", "r") as f:
    line = f.readline().strip()

print("First Gold Star:", firstGoldStar(line, 25))
print("Second Gold Star:", firstGoldStar(line, 75))
