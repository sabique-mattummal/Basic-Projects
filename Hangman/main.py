
import random
from hangman_words import word_list
from hangman_art import stages

#Picking a random word 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


#Game initialisation
end_of_game = False
lives = 6

print("Hangman Game")


# Creating blanks for guessing words

display = []

for _ in range(word_length):
    display += "_"

 #Game Brain
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    #console
    print(stages[lives])
