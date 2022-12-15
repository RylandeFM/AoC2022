with open("Input/Day 14.txt", "r") as f: inputString = f.read().splitlines()

def createBlockMap():
    blockingPoints = set()

    for line in inputString:
        splits = line.split(" -> ")
        for i, start in enumerate(splits[:-1]):
            x, y = [int(x) for x in start.split(",")]
            xEnd, yEnd = [int(x) for x in splits[i+1].split(",")]
            if x==xEnd: #vertical line
                for j in range(min(y, yEnd), max(y, yEnd)+1): blockingPoints.add((x, j))
            else: #horizontal line
                for j in range(min(x, xEnd), max(x, xEnd)+1): blockingPoints.add((j, y))

    return blockingPoints

def dropSand(bottomEdge):
    blockMap = createBlockMap()
    lowestPoint = max([y for _, y in blockMap])
    sandStart = (500, 0)
    sandCurrent = (sandStart[0], sandStart[1])
    sandResting = 0

    while (not bottomEdge and sandCurrent[1] <= lowestPoint) or (bottomEdge and sandStart not in blockMap):
        #falling
        if bottomEdge and sandCurrent[1] == lowestPoint + 1:
            sandResting += 1
            blockMap.add(sandCurrent)
            sandCurrent = (sandStart[0], sandStart[1])
            continue
        if (sandCurrent[0], sandCurrent[1] + 1) not in blockMap: 
            sandCurrent = (sandCurrent[0], sandCurrent[1] + 1)
            continue
        elif (sandCurrent[0] - 1, sandCurrent[1] + 1) not in blockMap: 
            sandCurrent = (sandCurrent[0] - 1, sandCurrent[1] + 1)
            continue
        elif (sandCurrent[0] + 1, sandCurrent[1] + 1) not in blockMap: 
            sandCurrent = (sandCurrent[0] + 1, sandCurrent[1] + 1)
            continue

        #no further
        sandResting += 1
        blockMap.add(sandCurrent)
        sandCurrent = (sandStart[0], sandStart[1])

    print(sandResting)

dropSand(False)
dropSand(True)