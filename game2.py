import random
 
def start_game():
    low = 1
    high = 10
    secret_number = random.randint(low, high)
    
    #This is a Test Line 
    print("The number is {}".format(secret_number))
    
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
    print("The current high score is {}, held by {}. Try and beat it!".format(high_score[0], first_place[0])) 
    
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
            high_score.sort()
            if high_score[0] > attempts:
                first_place[0] = input("What is your name? ")
                high_score.insert(0, attempts)
                
                print("You have the new high score!")
            else:
                print("The high score is currently {}, held by {}".format(high_score[0], first_place[0]))
                
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
    high_score = [7]
    first_place = ["Jim-Bob"]    
    start_game()
