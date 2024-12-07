from itertools import product

f = open("Input Files/input7.txt","r")
lines = f.readlines()


def firstGoldStar(lines):
    count = 0

    for line in lines:
        line = line.strip()
        key, values = line.split(":")
        expectedNumb = int(key)
        numbsToCompute = list(map(int, values.strip().split()))
        
        operations = ['+', '*']
        operation_combinations = product(operations, repeat=len(numbsToCompute) - 1)
        
        for ops in operation_combinations:
            result = numbsToCompute[0]
            
            for num, op in zip(numbsToCompute[1:], ops):
                if op == '+':
                    result += num
                elif op == '*':
                    result *= num
            
            if result == expectedNumb:
                count += expectedNumb
                break


    return count


def secondGoldStar(lines):
    count = 0

    for line in lines:
        line = line.strip()
        key, values = line.split(":")
        expectedNumb = int(key)
        numbsToCompute = list(map(int, values.strip().split()))
        
        operations = ['+', '*', "||"]
        operation_combinations = product(operations, repeat=len(numbsToCompute) - 1)
        
        for ops in operation_combinations:
            result = numbsToCompute[0]
            
            for num, op in zip(numbsToCompute[1:], ops):
                if op == '+':
                    result += num
                elif op == '*':
                    result *= num
                elif op == "||":
                    result = int(str(result) + str(num))
            
            if result == expectedNumb:
                count += expectedNumb
                break


    return count


print("First Gold Star:", firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))

        