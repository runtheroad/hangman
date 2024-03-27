# Hangman Game

This repository contains a simple implementation of the classic Hangman game in Python. The game selects a random word from a predefined list, and the player must guess the word one letter at a time

## How to Play

1. Start the game by running `python hangman.py` in your terminal
2. The game will present you with a series of underscores representing the letters of the randomly selected word
3. Type a letter and press Enter to make a guess
   - If the letter is in the word, the game will reveal its position(s)
   - If the letter is not in the word, you will lose an attempt
4. You have 6 incorrect guesses before the game ends
5. Guess the word before running out of attempts to win

## Features

- Simple text-based interface
- Random word selection from separate dictionary in .txt format
- Every word has a hint associated with it to make the guessing experience more fun and engaging
- Replayability: Option to start a new game or quit after each round

## Future Improvements

- Implement difficulty levels
- Implement scores


Enjoy the game, and may your guesses be lucky!
