import random


def numGuessGame():
    ranNum = random.randint(1, 20)
    print(ranNum)
    userGuess = int(input("Guess the number 1 to 20: "))
    while userGuess != ranNum:
        print("Incorrect try again !")
        userGuess = int(input("Guess again! "))
    else:
        print ("You win!")
    


numGuessGame()
