#Mastermind Script

#Function which will return is the permutation would return the same thing as the guess
def checkGuess(permutation, guess):
    numBlack = 0
    numWhite = 0
    detectedWhiteColors = []
    goodIndexes = []
    for x in range(0,4):
        if(permutation[x] == guess[x]):
            goodIndexes.append(x)
            numBlack+=1
    for x in range(0,4):
        #If the value is not equal
        if(permutation[x] != guess[x]):
            #Try to find a value in guess that is the same - That index can't be solved though.
            for y in range(0,4):
                if(permutation[x] == guess[y] and x != y and y not in goodIndexes):
                    if(permutation[x] not in detectedWhiteColors):
                        numWhite += 1
                        detectedWhiteColors.append(permutation[x])
    #print("Black : " + str(numBlack) + " White : " + str(numWhite))
    if(numBlack is guess[4] and numWhite is guess[5]):
        return True
    return False

#Creating the keyset(All Marble Colors)
keys = ['Red','Orange','Yellow','Green','Blue','Purple']#Temporary Keys
keys = ['R','W','Y','G','Bu','Bk']#Keys to be used

Guesses = []

#The guesses & responses from each guess
Guesses.append(['Y','G','R','Bk',0,2])
Guesses.append(['Bk','W','Y','Bu',1,1])
Guesses.append(['G','Bu','W','R',1,1])
Guesses.append(['W','R','Bk','R',0,1])
Guesses.append(['R','R','G','G',1,1])

#Making a list of all the possible permutations
allPermutations = []
for a in range(0, len(keys)):
    for b in range(0, len(keys)):
        for c in range(0, len(keys)):
            for d in range(0, len(keys)):
                allPermutations.append([keys[a],keys[b],keys[c],keys[d]])

solutionSet = []
for permutation in allPermutations:
    #print(permutation)
    #Checking to see if the permutation is still valid after comparing with the guesses
    isGood = True
    for guess in Guesses:
        if(not checkGuess(permutation, guess)):
            isGood = False
    if isGood:
        solutionSet.append(permutation)

#Printing all the possible solutions.
print("Solutions :")
for solution in solutionSet:
    print(solution)
