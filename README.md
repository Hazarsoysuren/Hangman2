# Hangman
Hangman is a Python terminal game, which can be ran on ide's like VScode and Replit for example.

Users can try to beat the game by guessing which word the machine has generated, There limited guesses and if you get the word correct you win.


## How to play

This Hangman is a guessing game made with python. The machine picks out a word out of the wordlist file, and the player tries to guess it by suggesting letters within a certain number of guesses. 

It looks like this. ![Image of hangman game](https://github.com/Hazarsoysuren/Hangman/blob/main/images/hangman.png?raw=true)

Start the Game: Launch the Hangman game either by running the Python script or executing the executable file, depending on how it's been packaged.

Guess the Word: The game will display a series of dashes representing the letters of the hidden word. Guess letters one at a time by typing them on your keyboard.

Correct Guesses: If your guessed letter is in the word, the game will reveal all occurrences of that letter in the word. You can continue guessing more letters.

Incorrect Guesses: If your guessed letter is not in the word, a part of the hangman will be drawn. Be careful! If too many incorrect guesses are made, the hangman will be completed, and you lose the game.

Complete the Word: Keep guessing letters until you either guess the entire word correctly or make too many incorrect guesses and the hangman is complete.

Win or Lose: If you guess the word correctly before the hangman is complete, you win! Otherwise, if the hangman is completed, you lose.

Play Again: After the game ends, you can choose to play again and try your luck at guessing a new word.


## Strategy

I made flowchart to plan each step to get this project functioning and to know the logic behind it, heres an image of it ![image of flowchart](https://github.com/Hazarsoysuren/Hangman/blob/main/images/flowchart.png?raw=true)

## Data model 
The data model in this Hangman project involves several components:

Word List:

- The word_list variable contains a list of words from which the Hangman game randomly selects a word for the player to guess. This data structure provides a pool of words for gameplay variation.

Chosen Word:

- The chosen_word variable stores the word randomly chosen from the word_list. This word serves as the target for the player to guess throughout the game.

Word Length:

- The word_length variable holds the length of the chosen_word, which is used to determine the number of blanks displayed to the player at the beginning of the game.

Display:

- The display list represents the current state of the word being guessed by the player. Initially, it contains underscores representing unrevealed letters, and as correct letters are guessed, underscores are replaced with the corresponding letters.

Lives:

- The lives variable tracks the number of attempts remaining for the player to guess the word. The game typically ends when the player exhausts all their lives.

End of Game Flag:

- The end_of_game variable is a boolean flag that indicates whether the game has concluded. It becomes True when either the player wins by guessing the word correctly or loses by running out of lives.

## Features 
Word List Customization:

- Users can customize the word list by adding, removing, or modifying words, allowing for a personalized gameplay experience.

ASCII Art Logo:

- A visually appealing ASCII art logo is displayed at the start of the game, adding to the thematic presentation.

Dynamic Display of Guessed Letters:

- The display dynamically updates to reveal correctly guessed letters within the word, helping players track their progress.

Visual Representation of Hangman:

- A visual representation of the Hangman's gallows and drawing progressively changes with each incorrect guess, adding suspense to the game.

Win/Loss Conditions:

- Players win upon correctly guessing the word and lose if they exhaust all their lives without guessing correctly.

Modular Architecture:

- The project adopts a modular architecture, separating concerns into distinct files/modules for word list management, ASCII art display, and game logic, promoting code organization and maintainability.

## Testing
I have tested this code through this [online website](www.online-ide.com) without any errors.

As well for no problems showing in my ide

### Bugs
**Solved bugs**
- I figured out to later to wrap the game code around a while loop to let the player i have more lives to continue

**Remaining bugs**
- No bugs remaining

### Validator testing
- Online-ide
      - No errors were returned


## Credits 
I made the ascii art by getting help from this [website](https://www.instructables.com/ASCII-Art/)

I also got much help from [W3schools](https://www.w3schools.com) and [geeksforgeeks](www.geeksforgeeks.org)

## Deployment
This project was deployed using Code Institute's mock terminal for Heroku
- Steps for deployment
   - Fork or clone this repository
   - Create a new Heroku app
   - Set the buildbacks to python and NodeJS in that order
   - Link the Heroku app to the repository
   - Click on **Deploy**


## Credits
- Code institute for the deployment terminal
- Iam also very grateful for my mentor to helping me with this project
