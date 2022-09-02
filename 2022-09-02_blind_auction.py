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

stop_bidding = False
bidding_enteries = {}

while not stop_bidding:
    name = input("What is your name ?: " )
    bid = int(input("What is your bid?: "))
    bidding_enteries[name] = bid

    more_user = (input("Are there any other bidders? Type 'yes' or 'no'. ")).lower()
    if more_user == 'no':
        stop_bidding = True

    sleep(1)
    os.system('cls')

print(bidding_enteries)

max_bid = 0
winner_name = ''

for key in bidding_enteries:
    if bidding_enteries[key] > max_bid:
        max_bid = bidding_enteries[key]
        winner_name = key
print()

sleep(1)
os.system('cls')
print(f"The winner is {winner_name} with a bid of ${bidding_enteries[winner_name]}.")