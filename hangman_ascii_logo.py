import pyfiglet

def hangman_ascii():
    # Function to generate ASCII art from text
    def generate_ascii_art(text):
        return pyfiglet.figlet_format(text)

    word_to_display = "hangman"
    ascii_art = generate_ascii_art(word_to_display)
    print(ascii_art)
