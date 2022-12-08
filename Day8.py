from functools import reduce

with open("Input/Day 8.txt", "r") as f: inputString = f.read().splitlines()

treeMap = []
for line in inputString:
    treeMap.append(list([int(x) for x in line]))

def scoreAxisFromTree(axis, start, stop, step, tree, height):
    score = 0

    for i in range(start, stop, step):
        score += 1
        if axis == "x":
            if treeMap[tree[1]][i] >= height: break
        else:
            if treeMap[i][tree[0]] >= height: break
            
    return score

def checkVisible(axis, start, stop, step):
    visible = set()

    for axis1 in range(len(treeMap)):
        highest = -1
        for axis2 in range(start, stop, step):
            if axis == "x":
                if treeMap[axis2][axis1] > highest: visible.add((axis1, axis2))
                highest = max(highest, treeMap[axis2][axis1])
            else:
                if treeMap[axis1][axis2] > highest: visible.add((axis2, axis1))
                highest = max(highest, treeMap[axis1][axis2])

    return visible

def findBestSpot():
    visible = set()
    
    visible.update(checkVisible("x", 0, len(treeMap), 1)) #look from top
    visible.update(checkVisible("x", len(treeMap)-1, -1, -1)) #look from bottom
    visible.update(checkVisible("y", 0, len(treeMap), 1)) #look from left
    visible.update(checkVisible("y", len(treeMap)-1, -1, -1)) #look from right
    
    print(len(visible))
    
    nonEdges = [(x, y) for (x, y) in visible if (x not in [0, len(treeMap[0])-1] and y not in [0, len(treeMap)-1])]
    
    highScore = 0

    for tree in nonEdges:
        height, scores = treeMap[tree[1]][tree[0]], []

        scores.append(scoreAxisFromTree("x", tree[0] + 1, len(treeMap[0]), 1, tree, height)) #score right
        scores.append(scoreAxisFromTree("x", tree[0] - 1, -1, -1, tree, height)) #score left    
        scores.append(scoreAxisFromTree("y", tree[1] + 1, len(treeMap[0]), 1, tree, height)) #score bottom       
        scores.append(scoreAxisFromTree("y", tree[1] - 1, -1, -1, tree, height)) #score top

        highScore = max(highScore, reduce((lambda x, y: x * y), scores))

    print(highScore)

findBestSpot()