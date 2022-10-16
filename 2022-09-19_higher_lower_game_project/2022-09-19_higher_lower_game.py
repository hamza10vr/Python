# Break down the Problem
# games ends when you guess wrong and prints your score
# randomly picks 2 celebrities compare A against B
# clears screen at each  answer and updates the score
# winner becomes A and pops a new B
# prints final answer when you are wrong
# Sorry, that's wrong. Final score: 3
from re import A
import art
import game_data
import random

def compare_followers(dict_a, dict_b):
    if dict_a > dict_b:
        return dict_a
    else:
        return dict_b

# TODO: list
#logo
print(art.logo)

#compare A: name, a description, from country
celebrity_a = random.choice(game_data.data)
print(celebrity_a)

#logo vs 
print(art.vs)
#Against B: name, a description, from country
celebrity_b = random.choice(game_data.data)
print(celebrity_b)
#who has more followers? Type 'A' or 'B': 
choice = input("Who has more followers? Type 'A' or 'B': ")
correct_answer = compare_followers(celebrity_a,celebrity_b)


# Display art

# Generate a random account from the game data

# format the account data into printable format.

# Ask user for a guess

# check if user is correct. 
## get follower count of each account.
## use if statement to check if user is correct.

# give user feedback on their guess.

# score keeping.

# Make the game repeatable.

# Making th account at position B become the next account at position A

# Clear the screen between rounds