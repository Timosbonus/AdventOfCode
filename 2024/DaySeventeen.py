with open("Input Files/input17.txt", "r") as f:
    lines = f.readlines()

def createRegisterMap(lines):
    registers = dict()
    for line in lines:
        line.strip()
        if "Register A" in line:
            registers["A"] = int(line[12:])
        elif "Register B" in line:
            registers["B"] = int(line[12:])
        elif "Register C" in line:
            registers["C"] = int(line[12:])
    return registers

def createProgram(lines):
    nums = list()
    for line in lines:
        if "Program" in line:
            line = line.strip()
            nums = [int(x) for x in line[9:].split(",")]
    return nums

def getComboOp(operand, registers):
    if operand == 4:
        return registers["A"]
    elif operand == 5:
        return registers["B"]
    elif operand == 6:
        return registers["C"]
    return operand

def adv(operand, registers):
    # combo operator
    registers["A"] = registers["A"] // 2 ** getComboOp(operand,registers)

def bxl(operand, registers):
    # literal operator
    registers["B"] = operand ^ registers["B"]

def bst(operand, registers):
    # combo
    registers["B"] = getComboOp(operand, registers) % 8

def jnz(index, operand, registers):
    # need continue statement in loop to not increase after
    if registers["A"] == 0: return index
    return operand

def bxc(registers):
    registers["B"] = registers["B"] ^ registers["C"]

def out(operand, registers):
    # combo
    ans = getComboOp(operand, registers) % 8
    return ","+str(ans)

def bdv(operand, registers):
    # combo operator
    registers["B"] = registers["A"] // 2 ** getComboOp(operand, registers)

def cdv(operand, registers):
    # combo operator
    registers["C"] = registers["A"] // 2 ** getComboOp(operand, registers)

def performChanges(registers, nums):
    output = ""
    index = 0

    while index <= len(nums) - 2: # jumps of two
        opCode, operand = nums[index], nums[index + 1]
        if opCode == 0:
            adv(operand, registers)
        elif opCode == 1:
            bxl(operand, registers)
        elif opCode == 2:
            bst(operand, registers)
        elif opCode == 3:
            newIndex = jnz(index, operand, registers)
            if index != newIndex:
                index = newIndex
                continue
        elif opCode == 4:
            bxc(registers)
        elif opCode == 5:
            output += out(operand, registers)
        elif opCode == 6:
            bdv(operand, registers)
        elif opCode == 7:
            cdv(operand, registers)
        index += 2
    
    return output[1:]   

def firstGoldStar(lines):
    registers = createRegisterMap(lines)
    nums = createProgram(lines)
    return(performChanges(registers, nums))
    

def secondGoldStar(lines):
    registers = createRegisterMap(lines)
    nums = createProgram(lines)
    sToCheck = ",".join(map(str, nums))
    index = 0
    while sToCheck != performChanges(registers, nums):
        index += 1
        registers = createRegisterMap(lines)
        registers["A"] = index
    return index
    


print("First Gold Star:", firstGoldStar(lines))
print("Second Gold Star:", secondGoldStar(lines))



