import random
import sys


#--------------Supporting functions----------------

def display(word):
    for letter in word:
        print(letter, end=' ')
    print()

def guessStatus(guessWordList):
    for letter in guessedWordList:
        if letter == '-':
            return False
    return True

# Actual game starts here

print("Welcome to Hangman!")

secretWords=['apple','banana','cherry','cat','dog','elephant','ocean','sea','puzzle']

secretWord = random.choice(secretWords) #picking a word randomly

secretWordLength= len(secretWord)

secretWordList= list(secretWord) # converting the word into the list for easy handling 
guessedWordList= ['-']* secretWordLength # we will update this list when user guess is correct
guessChances=secretWordLength+3

print(secretWord)
        
display(guessedWordList)

i=1
while i<=guessChances:

    guessedLetter = input('Guess a letter : ')

    if guessedLetter in secretWordList:
        indexOfLetter=secretWordList.index(guessedLetter)
        guessedWordList[indexOfLetter]=guessedLetter
        secretWordList[indexOfLetter]='*'

        display(guessedWordList)
        
        if guessStatus(guessWordList=guessedWordList):
            print("You Won the Math")
            sys.exit()

    else:
        print("Incorrect! ")
        display(guessedWordList)

    i+=1

print("You lossed the Match!")
    