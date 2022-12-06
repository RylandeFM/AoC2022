with open("Input/Day 6.txt", "r") as f: inputString = f.read()

def checkString(amountOfChars):
    for i in range(amountOfChars, len(inputString)):
        if len(set(inputString[i-amountOfChars:i])) == amountOfChars: return i

print(checkString(4))
print(checkString(14))