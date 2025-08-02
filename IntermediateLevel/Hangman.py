import random

# List of words for the game
words = ["python", "programming", "hangman", "developer", "algorithm"]

# Select a random word
word = random.choice(words)
word_length = len(word)

# Initialize variables
guessed_letters = set()  # Letters guessed by the player
attempts = 6  # Number of attempts
hangman_figure = [
    """
       -----
       |   |
           |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    """
]

# Game loop
while attempts > 0:
    # Display the current state of the word
    display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print(f"\nWord: {display_word}")
    print(hangman_figure[6 - attempts])  # Display hangman figure

    # Check if the player has guessed the word
    if display_word == word:
        print("Congratulations! You guessed the word!")
        break

    # Ask the player to guess a letter
    guess = input("Guess a letter: ").lower()

    # Validate the input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    # Add the guessed letter to the set
    guessed_letters.add(guess)

    # Check if the guessed letter is in the word
    if guess not in word:
        attempts -= 1
        print(f"Wrong guess! You have {attempts} attempts left.")

# End of game
if attempts == 0:
    print(hangman_figure[6])  # Display full hangman figure
    print(f"Game over! The word was: {word}")
