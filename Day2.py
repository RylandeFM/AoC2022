with open("Input/Day 2.txt", "r") as f: inputString = f.read().splitlines()

def playStrategies():
    score, moveSet = 0, {"A X": 4,"A Y": 8,"A Z": 3,"B X": 1,"B Y": 5,"B Z": 9,"C X": 7,"C Y": 2,"C Z": 6}
    score2, moveSet2 = 0, {"A X": 3,"A Y": 4,"A Z": 8,"B X": 1,"B Y": 5,"B Z": 9,"C X": 2,"C Y": 6,"C Z": 7}
    for play in inputString:
        score += moveSet[play]
        score2 += moveSet2[play]
    print(score)
    print(score2)
    
playStrategies()