import random
import collections


def addLetterAfterT():
    randomProba = random.random()
    if randomProba <= 0.1:
        return "T"
    elif randomProba <= 0.2:
        return "A"
    else:
        return "E"

def addLetterAfterE():
    randomProba = random.random()
    if randomProba <= 0.1:
        return "E"
    elif randomProba <= 0.2:
        return "T"
    else:
        return "A"

def addLetterAfterA():
    randomProba = random.random()
    if randomProba <= 0.1:
        return "A"
    elif randomProba <= 0.4:
        return "E"
    else:
        return "T"

def generateWord():
    generatedString = ""
    lastLetter = ""

    randomProba = random.random()

    if randomProba <= 0.333:
        generatedString = "T"
        lastLetter = addLetterAfterT()
    elif randomProba <= 0.666:
        generatedString = "E"
        lastLetter = addLetterAfterE()
    else:
        generatedString = "A"
        lastLetter = addLetterAfterA()

    generatedString += lastLetter

    if lastLetter == "T":
       lastLetter = addLetterAfterT()
    elif lastLetter == "E":
        lastLetter = addLetterAfterE()
    else:
        lastLetter = addLetterAfterA()

    generatedString += lastLetter

    return generatedString


words = []
tirages = 1000000
for i in range(tirages):
    words.append(generateWord())

cnt = collections.Counter(words)
print(cnt)


print("Proba : pour ", tirages, " tirages")

print('EAT', (cnt['EAT']/tirages)*100, '%')
print('ATE', (cnt['ATE']/tirages)*100, '%')
print('TEA', (cnt['TEA']/tirages)*100, '%')
