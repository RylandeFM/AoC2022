from math import lcm

with open("Input/Day 11.txt", "r") as f: inputString = f.read().splitlines()

monkeys = []

def readMonkeys():
    currentMonkey, dividerList = 0, []

    for line in inputString:
        if line[:6] == "Monkey":
            monkeys.append({"items": [], "op": "", "test": 0, "ifTrue": 0, "ifFalse": 0})
            currentMonkey = int(line.split()[1][0])
        elif "Starting items" in line:
            monkeys[currentMonkey]["items"] = [int(x) for x in line.split(":")[1].strip().split(",")]
        elif "Operation" in line:
            monkeys[currentMonkey]["op"] = line.split("=")[1].strip()
        elif "Test" in line:
            monkeys[currentMonkey]["test"] = int(line.split("by")[1].strip())
            dividerList.append(monkeys[currentMonkey]["test"])
        elif "If true" in line:
            monkeys[currentMonkey]["ifTrue"] = int(line.split("monkey")[1].strip())
        elif "If false" in line:
            monkeys[currentMonkey]["ifFalse"] = int(line.split("monkey")[1].strip())

    return dividerList

def monkeyThrow(rounds, worryDecay):
    mod = lcm(*readMonkeys())
    inspections = [0 for _ in range(len(monkeys))]
    
    for _ in range(rounds):
        for currentMonkey, monkey in enumerate(monkeys):
            for item in monkey["items"]:
                inspections[currentMonkey] += 1
                item = eval(monkey["op"].replace("old", str(item))) // worryDecay
                if item % monkey["test"] == 0:
                    monkeys[monkey["ifTrue"]]["items"].append(item % mod)
                else:
                    monkeys[monkey["ifFalse"]]["items"].append(item % mod)
            monkey["items"] = []

    inspections.sort(reverse=True)
    print(inspections[0] * inspections[1])

monkeyThrow(20, 3)
monkeyThrow(10000, 1)