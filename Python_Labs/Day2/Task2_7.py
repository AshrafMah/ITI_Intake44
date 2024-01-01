'''
Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of
which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word.
'''

import random

def chooseWord():
    words = ["facebook", "instagram", "twitter", "linkedin", "snapchat"]
    return random.choice(words)


def displayWord(word, guessedLetters):
    display = ''
    for letter in word:
        if letter in guessedLetters:
            display += letter
        else:
            display += '_'
    return display


def hangman():

    playerName = input("Enter your name: ")

    secretWord = chooseWord()
    guessedLetters = []
    attempts = 7

    while attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        if guess in guessedLetters:
            print("You've already guessed that letter. Try again.")
            continue

        guessedLetters.append(guess)

        if guess in secretWord:
            print("Good guess!")
        else:
            attempts -= 1
            print(f"Wrong guess! {attempts} attempts remaining.")

        currentDisplay = displayWord(secretWord, guessedLetters)
        print("Current word:", currentDisplay)

        if '_' not in currentDisplay:
            print("You guessed the word.")
            break

    if '_' in currentDisplay:
        print(f"Sorry, you ran out of attempts. The correct word is '{secretWord}'.")


if __name__ == "__main__":
    hangman()





