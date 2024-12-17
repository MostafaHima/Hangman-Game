from hangman_ascii_logo import hangman_ascii
import hangman_words
from hangman_ascii_art import HANGMANPICS
import random

# Generate random words of a specific length and count
word_list = hangman_words.generate_word_list(7, 100)

# Display ASCII art for Hangman
hangman_ascii()

# Select a random word from the list
random_word = random.choice(word_list)

# Function to convert the word into a format that can be guessed (e.g., '_')
def initialize_word(word):
    return ["_" for _ in word]

# Create a list to represent the letters of the word to be guessed
current_guess = initialize_word(random_word)
print(f"Initial Guess: {current_guess}")

remaining_lives = 6

# Main game loop
while "_" in current_guess and remaining_lives > 0:
    user_guess = input("Guess a letter: ").lower()


    # Function to check if the guessed letter is in the word
    def check_guess(guess, current_word, actual_word):
        updated_word = current_word[:]  # Copy the list to avoid modifying the original list
        if guess in actual_word:
            for index, letter in enumerate(actual_word):
                if guess == letter:
                    updated_word[index] = letter
            return updated_word, 0  # Correct guess, no life lost
        else:
            return updated_word, -1  # Incorrect guess, reduce lives


    # Call the check_guess function and update the list and lives
    updated_guess, life_change = check_guess(guess=user_guess, current_word=current_guess, actual_word=random_word)
    current_guess = updated_guess
    remaining_lives += life_change

    # Print the hangman image if the guess was incorrect
    if life_change == -1:
        print(HANGMANPICS[5 - remaining_lives])

    print(f"Current Guess: {current_guess}")
    print(f"Lives remaining: {remaining_lives}")

# Check win or lose conditions
if "_" not in current_guess:
    print("Congratulations! You won!")
else:
    print(HANGMANPICS[-1])  # Final hangman image
    print(f"Game Over! The word was: {random_word}")

    



