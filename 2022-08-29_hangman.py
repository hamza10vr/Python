# hangman game
# steps:
import random

word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word fromt eh word_list and assign it to a variable called chosed_word.
chosen_word = random.choice(word_list)
print(chosen_word)
# ask the user to guess a letter and assign their answer to a variable called gess. Make guess lowercase
guess = input("Guess a letter: ").lower()

# check if the letter the user guessed (guess) is one of the leters in the chosen_word)
for letter in chosen_word:
    if guess in chosen_word:
        print("Right!")
    else:
        print("wrong")