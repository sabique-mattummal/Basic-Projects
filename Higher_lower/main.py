from random import choice
from data import data

#Getting a random account from the list of accounts

def get_random_account():
    return choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'

def game():
    print("----Higher----\n <<  vs  >>\n____Lower____\n")
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"A : {format_data(account_a)}\nVs\nB"
              f" : {format_data(account_b)}")

        guess = input("Who has more follower ? Type 'A' or 'B' : \n").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print("Higher Vs Lower game")

        if is_correct:
            score += 1
            print(f"Right.\nCurrent Score {score}.")
        else:
            game_should_continue = False
            print(f"Wrong Answer.\nFinal Score : {score}")

game()

while input("Play Again ? Type 'y':  ").lower() == 'y':
    game()