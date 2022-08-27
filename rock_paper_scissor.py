rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]
user = int(
    input(
        'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'
    ))

if user >= 3 or user < 0:
    print("please type a valid nuber, you loose")
else:
    print(game_images[user])

    print('Computer chose:')
    computer = random.randint(0, 2)
    print(game_images[computer])

    if user == computer:
        print("It's a draw")
    elif user == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and user == 2:
        print("You lose!")
    elif user > computer:
        print("You win!")
    else:
        print("You lose!")
