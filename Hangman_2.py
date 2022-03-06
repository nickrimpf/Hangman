

#Hangman


import random

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''','''
    +---+
    0   |
        |
        |
       ===''','''
    +---+
    0   |
    |   |
        |
       ===''','''
    +---+
    0   |
   /|   |
        |
       ===''','''
    +---+
    0   |
   /|\  |
        |
       ===''','''
    +---+
    0   |
   /|\  |
   /    |
       ===''','''
    +---+
    0   |
   /|\  |
   / \  |
       ===''','''
    +---+
   [0   |
   /|\  |
   / \  |
       ===''','''
    +---+
   [0]  |
   /|\  |
   / \  |
       ===''']


words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wold wombat zebra'.split()


#This function returns a random string from the passed list of strings.
def getrandomword(WordList):
    wordIndex = random.randint(0, len(WordList) - 1)
    return WordList[wordIndex]

def displayboard(missedletters, correctletters, secretword):
    print(HANGMAN_PICS[len(missedletters)])
    print()

    print('Missed Letters:', end=' ')
    for letter in missedletters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretword)

    for i in range (len(secretword)): #Replace blanks with correct letters.
        if secretword[i] in correctletters:
            blanks = blanks[:i] + secretword[i] + blanks[i + 1:]

    for letter in blanks: #Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getguess(alreadyguessed): #Returns letter player entered. Function makes sure player entered a single letter and not something else.
    while True:
        print('Guess a letter')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter only one letter')
        elif guess in alreadyguessed:
            print('You already guessed that')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('LETTERS ONLY')
        else:
            return guess

def playagain(): #Function returns True if player wants to play again, otherwise it returns False
    print('Do you want to play again? (y or n)')
    return input().lower().startswith('y')


print(' H A N G M A N ')
missedletters = ''
correctletters = ''
secretword = getrandomword(words)
gameisdone = False

while True:
    displayboard(missedletters, correctletters, secretword)

    #Let player enter letter
    guess = getguess(missedletters + correctletters)

    if guess in secretword:
        correctletters = correctletters + guess

        #Check if player has won
        foundallletters = True
        for i in range(len(secretword)):
            if secretword[i] not in correctletters:
                foundallletters = False
                break
            if foundallletters:
                print('YES THE SECRET WORD IS "' + secretword + '"! YOU HAVE WON!')
                gameisdone = True

    else:
        missedletters = missedletters + guess

        #Check if player has guessed too many times
        if len(missedletters) == len(HANGMAN_PICS) - 1:
            displayboard(missedletters, correctletters, secretword)
            print('You have run out of guesses!\nAfter ' + str(len(missedletters)) + ' missed guesses ans ' +str(len(correctletters)) + ' correct guesses, the word was "' + secretword + '"')
            gameisdone = True

    #Ask to play again if game is done
    if gameisdone:
        if playagain():
            missedletters = ''
            correctletters = ''
            gameisdone = False
            secretword = getrandomword(words)
        else:
            break

    
        
                







