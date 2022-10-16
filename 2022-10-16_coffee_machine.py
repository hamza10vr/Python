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


def report(resources):
    """prints report of remaining resources"""
    return f"Water: {resources['water']}\n" \
           f"Milk: {resources['milk']}\n" \
           f"Milk: {resources['coffee']}\n"


# Initial prompt What would you like? (expresso/latte/cappuccino):
coffee_type = input("What would you like? (espresso/latte/cappuccino):  ").lower()
if coffee_type == 'report':
    print(report(resources))

# TODO: report - prints resources and money inserted

# TODO: prompt to insert money quarters, dimes, nickles, pennies, here is your change, here is your expresso repeat,
#  sorry not enough money and money refunded
# TODO: if resources not enough, sorry, not enough water etc
