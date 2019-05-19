#Mastermind Script
keys = ['Red','Orange','Yellow','Green','Blue','Purple']
keys2 = ['R','W','Y','G','Bu','Bl']
print(keys2)

Guesses = []
Guesses.append(['Blue','Red','Yellow','Purple',0,1])
Guesses.append(['Green','Purple','Yellow','Yellow',0,2])
Guesses.append(['Blue','Blue','Red','Green',1,0])
Guesses.append(['Purple','Orange','Red','Blue',2,0])
Guesses.append(['Red','Purple','Yellow','Green',1,1])

allPermutations = []
for a in range(0, len(keys)):
    for b in range(0, len(keys)):
        for c in range(0, len(keys)):
            for d in range(0, len(keys)):
                allPermutations.append([keys[a],keys[b],keys[c],keys[d]])
                #print([keys[a],keys[b],keys[c],keys[d]])

print("Length: " + str(len(allPermutations)))
solutionSet = []

def checkGuess(permutation, guess):
    numBlack = 0
    numWhite = 0
    whitePegColorsDetected = []
    if(permutation[0] == guess[0]):
        numBlack += 1
    elif(permutation[0] in guess and permutation[0] not in whitePegColorsDetected):
        whitePegColorsDetected.append(permutation[0])
        numWhite += 1

    if(permutation[1] == guess[1]):
        numBlack += 1
    elif(permutation[1] in guess and permutation[1] not in whitePegColorsDetected):
        whitePegColorsDetected.append(permutation[1])
        numWhite += 1

    if(permutation[2] == guess[2]):
        numBlack += 1
    elif(permutation[2] in guess and permutation[2] not in whitePegColorsDetected):
        whitePegColorsDetected.append(permutation[2])
        numWhite += 1

    if(permutation[3] == guess[3]):
        numBlack += 1
    elif(permutation[3] in guess and permutation[3] not in whitePegColorsDetected):
        whitePegColorsDetected.append(permutation[3])
        numWhite += 1

    #print(permutation)
    #print("Black : " + str(numBlack) + " White : " + str(numWhite))
    if(numBlack is guess[4] and numWhite is guess[5]):
        return True
    
    return False

for permutation in allPermutations:
    #Checking to see if the permutation would provide the same output if it was hidden based on a guess

    #Checking to see if the permutation satisfies all the guesses
    isGood = True
    for guess in Guesses:
        if(not checkGuess(permutation, guess)):
            isGood = False
    if isGood:
        solutionSet.append(permutation)

print(solutionSet)
