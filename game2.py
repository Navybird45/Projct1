"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    X1. Display an intro/welcome message to the player.
    X2. Store a random number as the answer/solution.
    X3. Continuously prompt the player for a guess.
      Xa. If the guess greater than the solution, display to the player "It's lower".
      Xb. If the guess is less than the solution, display to the player "It's higher".
    
    X4. Once the guess is correct, stop looping, inform the user they "Got it"
         Xand show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    low = 1
    high = 10
    secret_number = random.randint(low, high)
    #This is a Test Line 
    #print("The number is {}".format(secret_number))
    
    print("""
    ================================================
    Welcome to the Number Guessing Extravaganza!!!!
    ================================================
    """)
    
    print("""
    The rules are simple; choose a number between 1 
    and 10, and we will tell you if the secret 
    number is higher or lower than that. Try and 
    guess the secret number in as few guesses as
    possible!
    """)
    
    attempts = 0
    while True:
        try:
            guess = int(input("What is your guess?  "))
        except ValueError:
            print("Please enter a whole number!")
            continue
        if guess == secret_number:
            attempts += 1
            print("You got it!")
            print("You guessed the secret number in {} try(s)!".format(attempts))
            print("The high score is {}!".format(attempts))
            print("Thanks for playing!")
            replay = input("""Would you like to play again? [y]es or [n]o? """)
            if replay == "n":
                break
            if replay == "y":
                start_game()
                
        if 1 <= guess < secret_number:
            attempts += 1
            print("Too low!")
            continue
        if 11 >= guess > secret_number:
            attempts += 1
            print("Too high!")
            continue
        if guess > 10:
            print("The number must be between 1 and 10.")
            continue
        if guess < 1:
            print ("The number must be between 1 and 10.")
            continue
    
    
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
