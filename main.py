import random
import hangman_art
import hangman_words

#LOGO
print(hangman_art.logo)

#For easy debug: word_list = ["ardvark", "baboon", "camel"]
#SET A WORD TO MEET THE GOAL
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)


#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#CREATE AN IMAGINARY LIST TO ACHIEVE THE GOAL IN CORRESPONDENCE TO THE SET WORD
#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#REPETITIVELY TAKE INPUT AND CHECK VARIOUS CONDITIONS
end_of_game = False
lives = 6
while not end_of_game:
    print("----------------------------------------------")
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed
    if guess in display:
        print("*******You've already guessed this letter. Try Again!*******")
    
    #CHECK GUESSED LETTER AND PLACE IT IN DISPLAY (GUESS IS CORRECT)
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #CHECK IF GUESS IS WRONG
    if guess not in chosen_word:
        print(f"*******Your guessed letter, '{guess}' is not in the word.********")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE.")

    #TURNING LIST INTO STRING TO DISPLAY CURRENT-MADE-WORD TO USER
    print(f"{' '.join(display)}")

    #ALL BLANKS FILLED
    if "_" not in display:
        end_of_game = True
        print("YOU WON.")

    #HANGMAN ART
    print(hangman_art.stages[lives])