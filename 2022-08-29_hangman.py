# hangman game
# steps:
import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


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

end_of_game = False
while not end_of_game: # while ends with False, while not ends with True

    guess = input("Guess a letter: ").lower()

    # check if the letter the user guessed (guess) is one of the leters in the chosen_word
    # and replace the blank list if it matches
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess       

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!!!")

##### another way to do the above  #########
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

