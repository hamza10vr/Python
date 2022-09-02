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

# print(bidding_enteries) // for debugging


def find_highest_bidder(bidding_record):
    winner_name = ''
    max_bid = 0
    for bidder in bidding_enteries:
        if bidding_enteries[bidder] > max_bid:
            max_bid = bidding_enteries[bidder]
            winner_name = bidder
    print(f"The winner is {winner_name} with a bid of ${max_bid}.\n")

sleep(1)
os.system('cls')
find_highest_bidder(bidding_enteries)