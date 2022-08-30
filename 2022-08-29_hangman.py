# hangman game
# steps:
import random

word_list = ["ardvark", "baboon", "camel"]

# Randomly choose a word fromt eh word_list and assign it to a variable called chosed_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#create blank string equivalent to the lenght of the chosen_word
display = []
for _ in range(len(chosen_word)):
    display += "_"
print(display)

# ask the user to guess a letter and assign their answer to a variable called gess. Make guess lowercase
while "_" in display:

    guess = input("Guess a letter: ").lower()

    # check if the letter the user guessed (guess) is one of the leters in the chosen_word
    # and replace the blank list if it matches
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            print("Right!")
            display[index] = guess       
        else:
            print("Wrong")
    print(display)

##### another way to do the above  #########
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

