with open("Input/Day 6.txt", "r") as f: inputString = f.read()

def checkString(amountOfChars):
    for i in range(len(inputString)-amountOfChars+1):
        if len(set(inputString[i:i+amountOfChars])) == amountOfChars: return i+amountOfChars

print(checkString(4))
print(checkString(14))