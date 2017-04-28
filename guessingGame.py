#Small guessing game, play the computer to see if you can guess

from random import randint

#TODO - make a case for 0 correct & input validation

def game():
    computer_digits = [str(randint(0,9)), str(randint(0,9)), str(randint(0,9))]
    print("computers numbers: ")
    print(computer_digits)
    isTrue = True
    while isTrue:
        user_guess = list(input("What is your guess? "))

        i = 0
        numCorrect = 0
        for compdigit in computer_digits:
            if compdigit == user_guess[i]:
                numCorrect += 1

                if numCorrect == 3:
                    print("You won!")
                    isTrue = False
            i += 1
        if numCorrect == 1:
            print("Just one, try again")
        elif numCorrect == 2:
            print("Close, almost there!")
game()
