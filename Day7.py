from functools import cache

with open("Input/Day 7.txt", "r") as f: inputString = f.read().splitlines()

def parseFileSystem():
    fs, currentDir = {'/': {'parentDir': '', 'subDirs': [], 'sizeOfFiles': 0}}, '/'
    for instr in inputString[2:]:
        instr = instr.split(" ")
        if instr[0] == "$" and instr[1] == "cd":
            currentDir = currentDir + "/" + instr[2] if instr[2] != ".." else fs[currentDir]['parentDir']
        elif instr[0] == "dir":
            fs[currentDir + "/" + instr[1]] = {'parentDir': currentDir, 'subDirs': [], 'sizeOfFiles': 0}
            fs[currentDir]['subDirs'].append(currentDir + "/" + instr[1])
        elif instr[0] != "$":
            fs[currentDir]['sizeOfFiles'] += int(instr[0])
    return fs

@cache
def getSize(curDir):
    totalSize = fs[curDir]['sizeOfFiles']
    for subDir in fs[curDir]['subDirs']:
        totalSize += getSize(subDir)
    return totalSize

def prepareForUpdate():
    folderSizes = {x: getSize(x) for x in fs.keys()}
    print(sum([x for x in folderSizes.values() if x <= 100000]))
    print(min([x for x in folderSizes.values() if x >= (30000000 - (70000000 - folderSizes['/']))]))

fs = parseFileSystem()
prepareForUpdate()