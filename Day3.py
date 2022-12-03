with open("Input/Day 3.txt", "r") as f: inputString = f.read().splitlines()

def partOne():
    sum = 0
    for line in inputString:
        dupeList = [x for x in set(line[:len(line)//2]) if x in set(line[len(line)//2:])]
        sum += getPriority(dupeList[0])
    print(sum)

def getPriority(c):
    return ord(c)-96 if c.islower() else ord(c)-38

def partTwo():
    sum = 0
    for index in range(0,len(inputString),3):
        dupeList = [y for y in set(inputString[index+2]) if y in [x for x in set(inputString[index+0]) if x in set(inputString[index+1])]]
        sum += getPriority(dupeList[0])
    print(sum)

partOne()
partTwo()