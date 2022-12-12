from collections import deque

with open("Input/Day 12.txt", "r") as f: inputString = f.read()

def makeHeightMap():
    HMap, start, end, starts = [], (0, 0), (0, 0), []

    for y, line in enumerate(inputString.splitlines()):
        row = []
        for x, c in enumerate(line):
            if c == "S":
                row.append(0)
                start = (x, y)
                starts.append((x, y))
            elif c == "E":
                row.append(25)
                end = (x, y)
            else:
                if c == "a": starts.append((x, y))
                row.append(ord(c)-97)
        HMap.append(row)

    return HMap, start, end, starts

def findShortestPath(allStarts):
    HMap, start, end, starts = makeHeightMap()
    candidates, visited = deque([(0, x) for x in starts]) if allStarts else deque([(0, start)]), set()
    
    while candidates:
        distance, currentPoint = candidates.popleft()
        currentHeight = HMap[currentPoint[1]][currentPoint[0]]

        if currentPoint == end: return distance
        if currentPoint in visited: continue

        visited.add(currentPoint)

        if currentPoint[0] > 0 and HMap[currentPoint[1]][currentPoint[0] - 1] - currentHeight <= 1: 
            candidates.append((distance + 1, (currentPoint[0] - 1, currentPoint[1])))
        if currentPoint[0] < len(HMap[0]) -1 and HMap[currentPoint[1]][currentPoint[0] + 1] - currentHeight <= 1:
            candidates.append((distance + 1, (currentPoint[0] + 1, currentPoint[1])))
        if currentPoint[1] > 0 and HMap[currentPoint[1] - 1][currentPoint[0]] - currentHeight <= 1: 
            candidates.append((distance + 1, (currentPoint[0], currentPoint[1] - 1)))
        if currentPoint[1] < len(HMap) -1 and HMap[currentPoint[1] + 1][currentPoint[0]] - currentHeight <= 1: 
            candidates.append((distance + 1, (currentPoint[0], currentPoint[1] + 1)))

print(findShortestPath(False))
print(findShortestPath(True))