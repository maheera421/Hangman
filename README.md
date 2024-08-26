# Hangman
# 🎮 Game Description:

This code represents a text-based Hangman game. Hangman is a word guessing game where the player must guess letters to fill in the blanks of a hidden word. The player has a limited number of lives, and if they guess incorrectly too many times, they lose. The objective is to guess all the letters in the word before running out of lives.


# 🚀 How the Game Works:

• The game starts by printing a Hangman logo using ASCII art.

• A random word is chosen from a list of words. 

• The code creates a list called display to represent the current state of the word being guessed. Initially, it contains underscores (_) in the same quantity as the letters in the chosen word.

• The game then enters a loop that continues until one of the end conditions is met (the player wins or loses). In each iteration of the loop:

a. The player is prompted to input a letter to guess.

b. The code checks if the guessed letter has already been guessed before. If yes, it informs the player and does not penalize them.

c. If the guessed letter is in the chosen word, it is revealed in the display list at the correct position(s).

d. If the guessed letter is not in the chosen word, the player loses a life (represented by the lives variable), and if they run out of lives (lives reach 0), the game ends, and the player loses.

e. The current state of the word (with guessed letters revealed and underscores for unrevealed letters) is displayed to the player.

f. The game checks if there are no underscores left in the display list, which means the player has successfully guessed all the letters. If so, the game ends, and the player wins.

g. At each step, a Hangman ASCII art corresponding to the remaining lives is printed to visually represent the Hangman figure. 

• The game ends, and a message is printed to inform the player if they won or lost.


# 📝 Code Specifications:

• The code imports two modules: hangman_art and hangman_words. 

• The game starts with 6 lives, but this can be adjusted by changing the lives variable.

• The player can input lowercase letters to make guesses.

• The game displays the current state of the word with underscores for unrevealed letters and reveals correctly guessed letters.

• The player wins by guessing all the letters before running out of lives, and they lose if they run out of lives.

• The Hangman figure is visually represented as ASCII art at different stages based on the number of remaining lives.








