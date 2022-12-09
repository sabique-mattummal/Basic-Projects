from random import *

#Card selection function and returns two cards

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = choice(cards)
    return card

#Calculate score of total cards in list through sum() method for list, 
    #BlackJAck condition provided as total score = 21 and number of cards are two
    #Card Ace could be valued either 1 or 11, as per the total score not greater than 21
    
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

#Compare scores and return results as win or lose

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Went over. Player lose."
    elif user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer has BlackJack. Player lose"
    elif user_score == 0:
        return "Player has BlackJack and Won"
    elif user_score > 21:
        return "You went over. Player lose"
    elif computer_score > 21:
        return "Computer went over. You win"
    elif user_score > computer_score:
        return "Player win"
    else:
        return "Player lose"

#Game Engine

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        user_cards.append(draw_card())
        computer_cards.append(draw_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Player Cards : {user_cards} and score :{user_score}")
        print(f"Computer first card : {computer_cards[0]}.")
        
        #Condition can cause end game
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass :")
            if user_should_deal == 'y':
                user_cards.append(draw_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(draw_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand :{user_cards}, final score : {user_score}")
    print(f"Computer final hand :{computer_cards}, final_score : {computer_score}")
    print(compare(user_score, computer_score))

while input("Play a game of BlackJack ?  'y' to continue or 'n' to close : ") == 'y':
    play_game()
