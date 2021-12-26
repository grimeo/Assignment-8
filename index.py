# Assignment 8

# Program 1: Lottery
# Create a program that ask 3 numbers (0-9) from the user.
# Generate 3 random winning numbers (0-9)
# Display “Winner” if all 3 input numbers matched the generated numbers Display ”You loss” if not
# Display ”Try again y/n” after each game
# If the user enter “y” the user will play again
# if “n” the program will exit.

import random

print("Welcome to program 1 of Assignment 8!\n")
print("Program 1: Lottery\n")

# user input
def askForInputs():
    global num1, num2, num3
    num1 = str(input("Type the 1st number: "))
    num2 = str(input("Type the 2nd number: "))
    num3 = str(input("Type the 3rd number: "))

# random numbers
def generateNumbers():
    global n1, n2, n3
    n1 = random.randint(0,9)
    n2 = random.randint(0,9)
    n3 = random.randint(0,9)

# print the randoms (optional)
def printRandoms():
    print("Winning #1: " + str(n1) + "\nWinning #1: " + str(n2) +"\nWinning #1: " + str(n3))

def askToPlayAgain():
    playAgain = str(input("Try again? Y/N"))
    
    if playAgain.casefold() == "y":
        #play again
        print("play again")
    if  playAgain.casefold() == "n":
        # stop the program
        print("stop")


# check if the player won and if he want to play again
def checkIfMatched():
    if num1 == n1:
        if num2 == n2:
            if num3 == n3:
                print("Winner")
            else:
                print("You loss")
        else:
            print("You loss")
    else:
        print("You loss")
        


# --- main ---

    

# Program 2: Guess the number
# Generate 1 random number (0-100)

# Ask the user to guess the number
# Display “Greater than” if the inputed number is greater than the random number Display “Less than” 
# if the inputed number is less than the random number Repeat asking the user until the random number has been guessed correctly.