f = open("Input Files/input2.txt","r")
lines = f.readlines()




def checkDecrease(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] >= nums[i] or nums[i] - nums[i + 1] > 3:
            return False
    return True

def checkIncrease(nums):
    for i in range(len(nums) - 1):
        if nums[i + 1] <= nums[i] or nums[i + 1] - nums[i] > 3:
            return False
    return True

def firstGoldStar(lines):

    count = 0

    for line in lines:
        stringNums = line.split()
        nums = [int(cur) for cur in stringNums]

        actual = False

        if nums[0] > nums[1]: 
            actual = checkDecrease(nums)
        else: 
            actual = checkIncrease(nums)
        
        if actual: 
            count = count + 1
            print(nums)

    return count



def checkDecreaseTwo(nums):
    if checkDecrease(nums) == True:
        return True
    else:
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1] or nums[i] - nums[i + 1] > 3:
                if checkDecrease(nums[:i] + nums[i + 1:]) or len(nums) - i - 2 >= 0 and checkDecrease(nums[:i + 1] + nums[i + 2:]):
                    return True
                break

    return False

def checkIncreaseTwo(nums):
    nums = nums[:]
    if checkIncrease(nums) == True:
        return True
    else:
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1] or nums[i + 1] - nums[i] > 3:
                if checkIncrease(nums[:i] + nums[i + 1:]) or len(nums) - i - 2 >= 0 and checkIncrease(nums[:i + 1] + nums[i + 2:]):
                    return True
                break

    return False


def secondGoldStar(lines):

    count = 0

    for line in lines:
        stringNums = line.split()
        nums = [int(cur) for cur in stringNums]

        if checkDecreaseTwo(nums) or checkIncreaseTwo(nums):
            #print(nums)
            count = count + 1

    return count


