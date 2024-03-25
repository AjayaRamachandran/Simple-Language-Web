###### IMPORT ######
import random

###### INITIALIZE ######
sample = open("sample.txt", "r")
PUNCTUATION = [".",",","!","?","'",'"']
wordlist = []

LENGTH = 200

###### FUNCTIONS ######

def parseText():
    global wordlist, endersList, beginnersList
    wordlist = []
    endersList = []
    beginnersList = []
    firstWord = False
    for line in sample:
        row = line.strip()
        wordBuffer = ""
        for letter in range(len(row)):
            if row[letter] in PUNCTUATION:
                if row[letter] in [".", "!", "?"]:
                    endersList.append(wordBuffer)
                    firstWord = True
            elif row[letter] == " ":    
                wordlist.append(wordBuffer)
                if firstWord and row[letter - 1] not in PUNCTUATION:
                    beginnersList.append(wordBuffer)
                    firstWord = False
                wordBuffer = ""
            else:
                wordBuffer = wordBuffer + row[letter].lower()
    #print(beginnersList)

def findCandidates(word):
    candidateList = []
    for index, item in enumerate(wordlist):
        if item == word and index != len(wordlist) - 1:
            candidateList.append(wordlist[index + 1])
    #print(candidateList)
    return random.choice(candidateList)


###### MAIN ######
parseText()

output = ""
firstWord = True

for link in range(LENGTH):
    if firstWord:
        nextWord = random.choice(beginnersList)
        firstWord = False
    else:
        nextWord = findCandidates(word)
    output = output + " " + nextWord
    if nextWord in endersList and random.randint(1,3) == 1:
        output = output + ". "
        firstWord = True
    word = nextWord
print(output)