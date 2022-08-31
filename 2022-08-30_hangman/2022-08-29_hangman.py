# hangman game
# steps:
import random
from  hangman_art import logo, stages
from hangman_words import word_list


lives = 6

# importing the logo
print(logo)

# Randomly choose a word fromt eh word_list and assign it to a variable called chosed_word.
chosen_word = random.choice(word_list)
print(f"Pssst, the solution is {chosen_word}")

#create blank string equivalent to the lenght of the chosen_word
display = []
for _ in range(len(chosen_word)):
    display += "_"

end_of_game = False
letter_already_guessed = []

while not end_of_game: # while ends with False, while not ends with True

    guess = input("Guess a letter: ").lower()
    

    if guess not in chosen_word:
        print(f"You guessed a letter {guess}, that's not in the word. You lose a life")
        lives -=1 
        if lives == 0:   
            end_of_game = True
            print("You loose")  
    else:
        if guess not in letter_already_guessed:
            letter_already_guessed.append(guess)
        else:
            print(f"You've already guessed {guess}")
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess

    print(f"{' '.join(display)}")  

    

    if "_" not in display:
        end_of_game = True
        print("You Win!!!")
 
    print(stages[lives])            

##### another way to do the above  #########
# for position in range(len(chosen_word)):
#     letter = chosen_word[position]
#     if letter == guess:
#         display[position] = letter

