from functools import reduce

with open("Input/Day 11.txt", "r") as f: inputString = f.read().splitlines()

monkeys, lcm = [], 1

def readMonkeys():
    global lcm
    currentMonkey = 0
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
            lcm *= monkeys[currentMonkey]["test"]
        elif "If true" in line:
            monkeys[currentMonkey]["ifTrue"] = int(line.split("monkey")[1].strip())
        elif "If false" in line:
            monkeys[currentMonkey]["ifFalse"] = int(line.split("monkey")[1].strip())

def monkeyThrow(monkeyList, rounds, worryDecay, useMod):
    readMonkeys()
    inspections = [0 for _ in range(len(monkeyList))]
    for _ in range(rounds):
        for currentMonkey, monkey in enumerate(monkeyList):
            for item in monkey["items"]:
                inspections[currentMonkey] += 1
                item = eval(monkey["op"].replace("old", str(item)))
                item = item // worryDecay
                if item % monkey["test"] == 0:
                    monkeyList[monkey["ifTrue"]]["items"].append(item % lcm if useMod else item)
                else:
                    monkeyList[monkey["ifFalse"]]["items"].append(item % lcm if useMod else item)
            monkey["items"] = []
    inspections.sort(reverse=True)
    print(inspections[0]*inspections[1])

monkeyThrow(monkeys, 20, 3, False)
monkeyThrow(monkeys, 10000, 1, True)