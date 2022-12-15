import re

with open("Input/Day 15.txt", "r") as f: inputString = f.read().splitlines()

dataSet = []
for line in inputString:
    xS, yS, xB, yB = map(int, re.findall(r"(-?\d+)", line))
    distance = abs(xS - xB) + abs(yS - yB)
    dataSet.append([(xS, yS), (xB, yB), distance])

def partOne(target):
    beaconsOnTarget = set()
    minX, maxX = 0, 0

    for sensor, beacon, distance in dataSet:
        if beacon[1] == target: beaconsOnTarget.add(beacon[0])
        lineImpact = distance - abs(sensor[1] - target)
        minX = min(sensor[0] - lineImpact, minX)
        maxX = max(sensor[0] + lineImpact + 1, maxX)

    print(maxX - minX - len(beaconsOnTarget))

def partTwo(bound):
    intersects, gradients = set(), set()

    for sensor, _, distance in dataSet:
        gradients.add((sensor[1] - (distance + 1)) - sensor[0])
        gradients.add((sensor[1] + (distance + 1)) + sensor[0])

    for gradient1 in gradients:
        for gradient2 in gradients:
            x, y = (gradient2-gradient1)//2, (gradient2+gradient1)//2
            if 0 <= x <= bound and 0 <= y <= bound: intersects.add((x, y))
    
    for intersect in intersects:
        furtherAway = 0
        for sensor, _, distance in dataSet:
            if abs(sensor[0] - intersect[0]) + abs(sensor[1] - intersect[1]) > distance: furtherAway += 1
        if furtherAway >= len(dataSet): return (intersect[0] * 4000000) + intersect[1]

partOne(2000000)
print(partTwo(4000000))

#Bruto Force solution
#def partTwo(bound):
#    for y in range(bound, 0, -1):
#        edges = []
#        for sensor, _, distance in dataSet:
#            lineImpact = distance - abs(sensor[1] - y)
#            edges.append((max(0, min(sensor[0] - lineImpact, bound)), max(0, min(sensor[0] + lineImpact + 1, bound))))
#        edges.sort()
#        expectedStart = 0
#        for start, end in edges:
#            if start > expectedStart: 
#                return (expectedStart * 4000000) + y
#            expectedStart = max(expectedStart, end)

