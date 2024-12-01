f = open("Input Files/input1", "r")
lines = f.readlines()



def secondGoldStar(lines):

    leftNums = []
    rightNums = []

    for line in lines:
        s = line.split()
        leftNums.append(int(s[0]))
        rightNums.append(int(s[1]))

    countMap = {}

    for num in rightNums:
        if num in countMap:
            countMap[num] = countMap.get(num) + 1
        else:
            countMap[num] = 1
        
    count = 0

    for num in leftNums:
        if num in countMap:
            count = count + num * countMap.get(num)

    return count



def firstGoldStar(lines):
    sum1 = []
    sum2 = []

    for line in lines:
        s = line.split()
        sum1.append(int(s[0]))
        sum2.append(int(s[1]))

    sum1 = sorted(sum1)
    sum2 = sorted(sum2)

    dif = 0

    for i in range(len(sum1)):
        dif = dif + abs(sum2[i] - sum1[i])

    return dif


print(firstGoldStar(lines))
print(secondGoldStar(lines))
