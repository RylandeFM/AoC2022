with open("Input/Day 4.txt", "r") as f: inputString = f.read().splitlines()

def checkContainment():
    fullyContained = 0
    partiallyContained = 0
    for line in inputString:
        elf1, elf2 = line.split(",")
        elfSet1, elfSet2 = set(range(int(elf1.split("-")[0]), int(elf1.split("-")[1])+1)), set(range(int(elf2.split("-")[0]), int(elf2.split("-")[1])+1))
        fullyContained += 1 if (len(elfSet1-elfSet2) == 0 or len(elfSet2-elfSet1) == 0) else 0
        partiallyContained += 1 if (len(elfSet1-elfSet2) < len(elfSet1)) else 0
    print(fullyContained)
    print(partiallyContained)

checkContainment()