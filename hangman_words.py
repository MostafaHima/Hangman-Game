import random
import string

# Function to generate a random word of a given length
def generate_word(length):
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for _ in range(length))

# Function to generate a list of random words with a specific length and count
def generate_word_list(word_length, word_count):
    return [generate_word(word_length) for _ in range(word_count)]




