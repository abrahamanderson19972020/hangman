import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages, logo

#Step 1: Import the word list to use the 'word_list' from hangman_words.py
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6

#Step 2: Import the logo from hangman_art.py and print it at the start of the game.
stages = stages
for stage in stages:
    print("These are the stages in the game...")
    print(stage)

#Testing code
print(logo)
print("The game is starting")


#Create blank list
display = []

for i in range(word_length): # add "_" for every letter in the chosen word
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()
    #Step 3: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed {guess}")

    #Check guessed letter and add the display list if the guess is correct
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Step 5:Check if user is wrong and decrease from the lives the user has
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, but this is in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f'The solution is {chosen_word}.')

    #Step 6: Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Step 7: Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    #Step 8: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])