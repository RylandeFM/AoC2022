with open("Input/Day 3.txt", "r") as f: inputString = f.read().splitlines()

def partOne():
    print(sum([getPriority((set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()) for line in inputString]))

def partTwo():
    print(sum([getPriority((set(inputString[index+2]) & set(inputString[index+0]) & set(inputString[index+1])).pop()) for index in range(0,len(inputString),3)]))

def getPriority(c):
    return ord(c)-96 if c.islower() else ord(c)-38

partOne()
partTwo()