MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def generate_report(resources, money):
    """prints report of remaining resources"""
    return f"Water: {resources['water']}\n" \
           f"Milk: {resources['milk']}\n" \
           f"Coffee: {resources['coffee']}\n" \
           f"Money: ${profit}\n"



def check_resources(order_ingredients):
    """Takes coffe input checks it against to resources to verify if enough ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is Not enough {item}")
            return False
        return True
def process_coins():
    """Returns teh total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total
def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient. """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False

is_on = True

while is_on:
    # Initial prompt What would you like? (expresso/latte/cappuccino):
    choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if choice == 'report':
        print(generate_report(resources, payment))
    elif choice == 'off':
        is_on = False
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            is_transaction_successful(payment, drink['cost'])

