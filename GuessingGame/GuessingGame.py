import random
import math


def game():
    # Define game details and print title
    cont = True

    # Start main game loop
    while cont:
        won = False
        correctchoice = False

        print("\nGuessing Game!\n")

        # Difficulty level choice loop
        while not correctchoice:
            difficulty = input("What difficulty level do you want to play? (E)asy, (M)edium or (H)ard ")
            if difficulty == "E":
                print ("Easy Difficulty\n")
                ceillimit = 25
                correctchoice = True
            elif difficulty == "M":
                print ("Medium Difficulty\n")
                ceillimit = 50
                correctchoice = True
            elif difficulty == "H":
                print ("Hard Difficulty\n")
                ceillimit = 100
                correctchoice = True
            else:
                print ("I didn't understand that.\n")

        # generate the number of guesses using log base 2
        guessno = round(math.log(ceillimit, 2))

        # Initialise game
        turn = 1

        # get random number
        num = random.randint(1, ceillimit)

        # Load intro text
        print("\n Guess a number between 1 and %d inclusive. You have %d attempts to guess the right number." % (ceillimit, guessno))

        # game loop
        while turn <= guessno:

            # ask user for input, check it is an integer only
            try:
                guess = int(input("Try %d: Enter your guess! " % turn))
            except NameError:
                print("That is not a whole number. Try again")
                continue
            except SyntaxError:
                print("That is not a whole number. Try again")
                continue
            except ValueError:
                print("That is not a whole number. Try again")
                continue

            if isinstance(guess, float):
                print("That is not a whole number. Try again")
                continue
            elif guess > ceillimit:
                print ("That's a bit too high, please guess a number between 1 and %d." % (ceillimit))
                continue

            # compare input to random number
            result = compareguess(guess, num)
            # calculate response
            if result == -1:
                print("That was too low, try again!")
            elif result == 0:
                won = True
                break
            elif result == 1:
                print("That was too high, try again!")
            else:
                print("Something has gone wrong!")
                break

            turn += 1

        # Checking for win/loss
        if not won:
            print("You have lost. The number was %d." % (num))
        else:
            print("Congratulations! the number was %d !\n You attempted this in %d tries!" % (num, turn))

        # prompt for new game
        choice = input("Do you want to play again? Y/N ")
        if choice != "Y":
            print("Thank you for the game!")
            cont = False


def compareguess(userinput, randomnumber):
    """Compare two numbers, and return if the user inputted number is equal to, lower or higher than the randomly
        generated number


    Parameters:
        userinput (int) :       The user's guess value as integer
        randomnumber (int) :    The random number to compare to

    Returns:
        result (int):   Returns an integer, -1, guess is lower than random num, 1, guess is higher than random num,
                        0 guess matches random num

    >>> compareguess(2,3)
    -1
    >>> compareguess(3,3)
    0
    >>> compareguess(4,3)
    1

    """

    if userinput < randomnumber:
        return -1
    elif userinput == randomnumber:
        return 0
    elif userinput > randomnumber:
        return 1


# Doctest the compare function
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    game()
