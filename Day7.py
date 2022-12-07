with open("Input/Day 7.txt", "r") as f: inputString = f.read().splitlines()

def parseFileSystem():
    fs, currentDir = {'/': {'parentDir':'', 'subDirs':[], 'files':[]}}, '/'
    for instr in inputString[2:]:
        instr = instr.split(" ")
        if instr[0] == "$" and instr[1]=="cd":
            currentDir = currentDir+"/"+instr[2] if instr[2] != ".." else fs[currentDir]['parentDir']
        elif instr[0] == "dir":
            fs[currentDir+"/"+instr[1]] = {'parentDir':currentDir, 'subDirs':[], 'files':[]}
            fs[currentDir]['subDirs'].append(currentDir+"/"+instr[1])
        elif instr[0] != "$":
            fs[currentDir]['files'].append((instr[1], int(instr[0])))
    return fs

def getSize(curDir, fs):
    totalSize = sum([x[1] for x in fs[curDir]['files']])
    for subDir in fs[curDir]['subDirs']:
        totalSize += getSize(subDir, fs)
    return totalSize

def prepareForUpdate():
    fs = parseFileSystem()
    folderSizes = {x: getSize(x, fs) for x in fs.keys()}
    print(sum([x for x in folderSizes.values() if x <= 100000]))
    print(min([x for x in folderSizes.values() if x >= (30000000 - (70000000 - folderSizes['/']))]))

prepareForUpdate()