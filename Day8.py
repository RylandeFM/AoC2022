from functools import reduce

with open("Input/Day 8.txt", "r") as f: inputString = f.read().splitlines()

treeMap = []
for line in inputString:
    treeMap.append(list([int(x) for x in line]))

def findBestSpot():
    visible = set()
    for x in range(len(treeMap[0])):
        highestTop, highestBottom = -1, -1
        for y in range(0,len(treeMap)):
            if treeMap[y][x] > highestTop:
                visible.add((x, y))
                highestTop = treeMap[y][x]

        for y in range(len(treeMap)-1, -1, -1):
            if treeMap[y][x] > highestBottom:
                visible.add((x, y))
                highestBottom = treeMap[y][x]

    for y in range(len(treeMap)):
        highestLeft, highestRight = -1, -1
        for x in range(len(treeMap[y])):
            if treeMap[y][x] > highestLeft:
                visible.add((x, y))
                highestLeft = treeMap[y][x]

        for x in range(len(treeMap[y])-1,-1,-1):
            if treeMap[y][x] > highestRight:
                visible.add((x, y))
                highestRight = treeMap[y][x]

    print(len(visible))
    
    nonEdges = [(x, y) for (x, y) in visible if (x not in [0, len(treeMap[0])-1] and y not in [0, len(treeMap)-1])]
    
    highScore = 0
    for tree in nonEdges:
        height, scores = treeMap[tree[1]][tree[0]], []
        score = 0
        for x in range(tree[0] + 1, len(treeMap[0])): #look right
            score += 1
            if treeMap[tree[1]][x] >= height: break
        scores.append(score)

        score = 0
        for x in range(tree[0] - 1, -1, -1): #look left
            score += 1
            if treeMap[tree[1]][x] >= height:
                break
                
        scores.append(score)

        score = 0
        for y in range(tree[1] + 1, len(treeMap[0])): #look bottom
            score += 1
            if treeMap[y][tree[0]] >= height:
                break
                
        scores.append(score)

        score = 0
        for y in range(tree[1] - 1, -1, -1): #look top
            score += 1
            if treeMap[y][tree[0]] >= height:
                break
                
        scores.append(score)
        highScore = max(highScore, reduce((lambda x, y: x * y), scores))

    print(highScore)

findBestSpot()