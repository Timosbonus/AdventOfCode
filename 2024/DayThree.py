import re

f = open("Input Files/input3.txt","r")
lines = f.readlines()


def secondGoldStar(lines):

    s = "".join(lines)

    pattern = r"don't\(\)[\s\S]*?do\(\)"
       
    modLine = re.sub(pattern, "", s)

    return firstGoldStar(modLine)
    



def firstGoldStar(lines):

    s = "".join(lines)

    count = 0
 
    pattern = r"mul\((\d+),(\d+)\)"

    matches = re.findall(pattern, s)

    for num1,num2 in matches:
        count += int(num1) * int(num2)


    return count

print(firstGoldStar(lines))
print(secondGoldStar(lines))
    