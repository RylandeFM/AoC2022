with open("Input/Day 10.txt", "r") as f: inputString = f.read().splitlines()

def partOne():
    register, interests, cycle = 1, [], 0
    currentPrint, screenLines = "", []

    for line in inputString:
        if line == "noop": 
            currentPrint += "#" if cycle % 40 in range(register - 1, register + 2) else "."
            cycle += 1
            if cycle % 40 == 20: interests.append(register * cycle)
        else:
            currentPrint += "#" if cycle % 40 in range(register - 1, register + 2) else "."
            cycle += 1
            if cycle % 40 == 20: 
                interests.append(register * cycle)
            elif cycle % 40 == 0:
                screenLines.append(currentPrint)
                currentPrint = ""

            currentPrint += "#" if cycle % 40 in range(register - 1, register + 2) else "."
            cycle += 1
            if cycle % 40 == 20: interests.append(register * cycle)

            register += int(line.split()[1])
            
        if cycle % 40 == 0:
            screenLines.append(currentPrint)
            currentPrint = ""

    print(sum(interests))
    for line in screenLines: print(line)

partOne()