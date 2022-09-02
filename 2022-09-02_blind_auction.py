from time import sleep
import os
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program")
name = input("What is your name ?:" )
bid = input("What is your bid?: ")


sleep(2)

os.system('cls')

name = input("What is your name?:" )
bid = input("What is your bid?: ")

stop_bidding = (input("Are there any other bidders? Type 'yes' or 'no'. ")).lower()

print(f"The winner is {} with a bid of ${}.")