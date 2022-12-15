import re
import time
with open("Input/Day 15.txt", "r") as f: inputString = f.read().splitlines()

dataSet = []
for line in inputString:
    xS, yS, xB, yB = map(int, re.findall(r"(-?\d+)", line))
    distance = abs(xS - xB) + abs(yS - yB)
    dataSet.append([(xS, yS), (xB, yB), distance])


def partOne(target):
    noBeacons = set()
    beaconsOnTarget = set()

    for sensor, beacon, distance in dataSet:
        if beacon[1] == target: beaconsOnTarget.add(beacon[0])
        lineImpact = distance - abs(sensor[1] - target)
        #If sensor is not relevant the range will have the first argument higher, skipping the sensor
        for x in range(sensor[0] - lineImpact, sensor[0] + lineImpact + 1): noBeacons.add(x)

    print(len(noBeacons-beaconsOnTarget))

def partTwo(bound):
    for y in range(bound):
        edges = []
        for sensor, _, distance in dataSet:
            lineImpact = distance - abs(sensor[1]-y)
            edges.append((max(0, min(sensor[0] - lineImpact, bound)), max(0, min(sensor[0] + lineImpact + 1, bound))))
        edges.sort()
        expectedStart = 0
        for start, end in edges:
            if start > expectedStart: return (expectedStart * 4000000) + y
            expectedStart = max(expectedStart, end)
start = time.perf_counter_ns()
partOne(2000000)
print(f'{(time.perf_counter_ns()-start)/1000000} ms')
start = time.perf_counter()
print(partTwo(4000000))
print(f'{(time.perf_counter()-start)} s')