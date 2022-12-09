with open("Input/Day 9.txt", "r") as f: inputString = f.read().splitlines()

def simulateRopes():
    visitedPart1, visitedPart2, movements = set(), set(), {'R':(1, 0), 'L':(-1, 0), 'U':(0, 1), 'D':(0, -1)}
    positions = [[0, 0] for _ in range(10)]
    for instr in inputString:
        direction, steps = instr.split(" ")
        for _ in range(int(steps)):
            positions[0] = [positions[0][0] + movements[direction][0], positions[0][1] + movements[direction][1]]
            for i in range(1, 10):
                if abs(positions[i][0] - positions[i - 1][0]) >= 2 or abs(positions[i][1] - positions[i - 1][1]) >= 2:
                    if positions[i][0] != positions[i - 1][0]:
                        positions[i][0] += 1 if positions[i - 1][0] > positions[i][0] else -1
                    if positions[i][1] != positions[i - 1][1]:
                        positions[i][1] += 1 if positions[i - 1][1] > positions[i][1] else -1
            visitedPart1.add((positions[1][0], positions[1][1]))
            visitedPart2.add((positions[9][0], positions[9][1]))
    print(len(visitedPart1))
    print(len(visitedPart2))

simulateRopes()