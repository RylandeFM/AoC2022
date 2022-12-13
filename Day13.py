from collections import deque
from turtle import left

with open("Input/Day 13.txt", "r") as f: inputString = f.read().splitlines()

def partOne():
    list1, list2, currentPair, goodIndex = [], [], 1, []
    for i, line in enumerate(inputString):
        if i % 3 == 2: 
            list1, list2 = [], []
            currentPair += 1
        if i % 3 == 0: list1 = deque(eval(line))
        if i % 3 == 1: 
            list2 = deque(eval(line))
            listEval, _ = evaluateLists(list1, list2)
            if listEval: goodIndex.append(currentPair)
    print(sum(goodIndex))

def evaluateLists(left, right):
    while True:
        if len(left) == 0 and len(right) == 0: return True, True #all tests passed in sub lists so inconclusive
        if len(left) == 0: return True, False #right list still has items
        if len(right) == 0: return False, False #left list still has items
        leftItem = left.popleft()
        rightItem = right.popleft()
        if isinstance(leftItem, int) and isinstance(rightItem, int):
            if leftItem == rightItem:
                continue
            else:
                return leftItem < rightItem, False #check on number
        else:
            if isinstance(leftItem, int): leftItem = [leftItem]
            if isinstance(rightItem, int): rightItem = [rightItem]
            listEval, inconclusive = evaluateLists(deque(leftItem), deque(rightItem))
            if inconclusive: continue #subList yielded no answer so move on to the next items
            return listEval, False

def partTwo():
    listToSort = deque()
    for line in inputString:
        if line != "": listToSort.append(deque(eval(line)))
    listToSort.append(deque([[2]]))
    listToSort.append(deque([[6]]))
    
    issueFound = True
    while issueFound:
        issueFound = False
        newList = deque()

        while len(listToSort) > 1:
            left = listToSort.popleft()
            right = listToSort.popleft()
            listEval, _ = evaluateLists(deque(left), deque(right))
            if listEval:
                newList.append(left)
                listToSort.appendleft(right)
            else:
                issueFound = True
                newList.append(right)
                listToSort.appendleft(left)
        newList.append(listToSort.pop())
        listToSort = newList

    decoderIndices = [i + 1 for i, item in enumerate([str(list(x)) for x in listToSort]) if item == "[[2]]" or item == "[[6]]"]
    print(decoderIndices[0] * decoderIndices[1])

partOne()
partTwo()