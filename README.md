# Hangman Game

## Description

This is a simple Hangman game implemented in Python. The game selects a random word, and the player must guess letters to figure out the word. The player has a limited number of incorrect guesses before they lose the game.

## Features

- ASCII art for the hangman drawing.
- Word list generated randomly with a specified length and count.
- Keeps track of lives and updates the hangman image for incorrect guesses.
- Displays the current state of the word as underscores (`_`) and fills in correct guesses.

## Requirements

- Python 3.x
- `pyfiglet` library for ASCII art rendering.

## Installation

To run this project, you'll need to have Python 3.x installed. You can install the required dependencies using pip:

```bash
pip install pyfiglet
```
## Usage
1. Clone the repository or download the project files.
2. Ensure all dependencies are installed.
3. Run the main.py script.
  ```bash
  python main.py
```
4. The game will prompt you to guess a letter. Type a letter and press Enter.
5. The game will display the current word and how many lives you have left.
6. Continue guessing until you either:
- Correctly guess the word (you win).
- Run out of lives (you lose).

## Game Flow
- The game starts by showing the hangman drawing.
- Each time you make an incorrect guess, the drawing updates.
- If you guess a letter correctly, it appears in the word.
- The game ends when you either guess the word or run out of lives.
