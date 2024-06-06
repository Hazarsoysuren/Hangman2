from hangman_art import logo, stages
from hangman_words import word_list
import random

def play_game():
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    
    end_of_game = False
    lives = 6

    # Print the logo at the start of the game
    print(logo)

    # Create blanks
    display = ["_" for _ in range(word_length)]
    guessed_letters = set()

    while not end_of_game:
        # Defensive programming to ensure person enters one alphabetic character
        character = ""
        while character == '':
            guess = input("Guess a letter: ").lower().strip()
            if guess.isalpha() and len(guess) == 1:
                character = guess
            else:
                print('No, you need to enter one alphabetic character!')

        # If the user has entered a letter they've already guessed, print the letter and let them know.
        if guess in guessed_letters:
            print(f"You've already guessed {guess}")
        else:
            guessed_letters.add(guess)

        # Check guessed letter
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        # Check if user is wrong.
        if guess not in chosen_word:
            # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            lives -= 1
            if lives == 0:
                end_of_game = True
                print("You lose.")
                print(f"The word was: {chosen_word}")

        # Join all the elements in the list and turn it into a String.
        print(f"{' '.join(display)}")

        # Display guessed letters
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        # Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

        # Print the current stage of the hangman
        print(stages[lives])

# Main game loop
while True:
    play_game()
    replay = input("Do you want to play again? Type 'yes' or 'no': ").lower()
    if replay != 'yes':
        break
print("Thanks for playing! Goodbye.")
