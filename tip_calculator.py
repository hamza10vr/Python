# if the bill was $100.000, split between 4 people with 12% tip.
# Each person should pay (100.00/4) * 1.12
# Round the results to 2 decimal places.

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give ? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip /100 * bill + bill
bill_per_person = round((bill_with_tip / people),2)
print(bill_per_person)