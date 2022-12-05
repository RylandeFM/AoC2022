from collections import deque
import re

with open("Input/Day 5.txt", "r") as f: inputString = f.read()

stacks, instructions = inputString.split("\n\n")
stacks = stacks.split("\n")
instructions = instructions.split("\n")

def parseInput():
    stackList, maxStacks, charsPerStack = [], max([int(x.strip()) for x in stacks[-1].split("   ")]), 4

    for stackNumber in range(maxStacks):
        column, index = deque(), stackNumber * charsPerStack + 1
        for line in range(len(stacks) - 1):
            if stacks[line][index] != " ": column.append(stacks[line][index])
        stackList.append(column)

    return stackList

def partOne():
    containers = parseInput()

    for instr in instructions:
        amount, source, dest = map(int, re.findall(r"(\d+)", instr))
        for _ in range(amount):
            containers[dest-1].appendleft(containers[source-1].popleft())
            
    print("".join([container[0] for container in containers]))

def partTwo():
    containers = parseInput()

    for instr in instructions:
        amount, source, dest = map(int, re.findall(r"(\d+)", instr))
        addList = []
        for _ in range(amount):
            addList.append(containers[source-1].popleft())

        for item in addList[::-1]:
            containers[dest-1].appendleft(item)
   
    print("".join([container[0] for container in containers]))

partOne()
partTwo()