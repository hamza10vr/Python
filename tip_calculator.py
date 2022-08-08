# if the bill was $100.000, split between 4 people with 12% tip.
# Each person should pay (100.00/4) * 1.12
# Round the results to 2 decimal places.

print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip_percentage = input("What percentage tip would you like to give ? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tip = 1+ (int(tip_percentage) /100)
total_bill = float(bill) * tip
per_person = float(round(total_bill/int(num_people),2))
print(f"Each person should pay:${per_person}" )
