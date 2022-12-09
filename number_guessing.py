from random import *
EASY_LEVEL = 10
HARD_LEVEL = 5

#Function to check player answer against computer pick

def check_answer(guess, answer, attempts):
    if guess > answer:
        print("Guessed a higher number. Choose a lower")
        return attempts - 1
    elif guess < answer:
        print("Guessed a lower number. Choose a Higher")
        return attempts - 1
    else:
        print(f"Correct answer : {answer}")

#Set difficulty function

def set_difficulty():
    level = input("Choose difficulty level\n"
                  "(Type 'e' for Easy, 'h' for Hard) :\n").lower()
    if level == 'e':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

#Game engine

def game():
    print("$$$ Number guessing game by python basic syntax $$$"
          "\nComputer guessed a number between 1 to 100")
    answer = randint(1, 100)

    attempts = set_difficulty()

    #Repeat the functionality

    guess = 0

    while guess != answer:
        print(f"{attempts} attempts left")
        guess = int(input("Guess a number :\n"))
        attempts = check_answer(guess, answer, attempts)
        if attempts == 0:
            print("Exceeded all attempts, Player lose\n"
                  f"Answer : {answer}")
            return
        elif guess != answer:
            print("Guess again")

game()





