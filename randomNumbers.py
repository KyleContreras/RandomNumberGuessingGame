#########################################################
#                                                       #
#                 Number Guessing Game!                 #
#                                                       #
#########################################################

import random

# Generate a random number between 1-100
intRandomNum = random.randint(1,101)

####### Test against the random number######
print(intRandomNum)                        #
############################################
# Initialize the var with the current student guess
intStudentGuess = int(input("Guess a number between 1 and 100!"))

# Total number of guesses taken
intGuessCount = 0

# while the condition is true, inform the player whether they are too high or too low in their guess
# keep track of number of guesses and accept a new guess.
while intStudentGuess != intRandomNum:  

    if intStudentGuess > intRandomNum:
        print("Too high")
    else:
        # If the number isn't too high, then it has to be too low.
        print("Too low")
    intGuessCount += 1
    intStudentGuess = int(input("Guess a number between 1 and 100!"))

# The while loop stops iterating once the condition is no longer true. The user got the correct answer.
# They are given confirmation, intGuessCount is incremented and the user is given the total number of tries.
intGuessCount = intGuessCount + 1
print ("Congratulations! " + str(intStudentGuess) + " is the correct answer!")
print ("It took you " + str(intGuessCount) + " tries to get it right.")
print ("Thank you for playing!")




