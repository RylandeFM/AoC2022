with open("Input/Day 1.txt", "r") as f: inputString = f.read().splitlines()

def countCalories():
    elvesCalories, currentList = [], []
    for item in inputString:
        if item == "":
            elvesCalories.append(sum(currentList))
            currentList=[]
        else:
            currentList.append(int(item))
    elvesCalories.append(sum(currentList))
    elvesCalories.sort(reverse=True)
    print(elvesCalories[0])
    print(sum(elvesCalories[0:3]))

countCalories()