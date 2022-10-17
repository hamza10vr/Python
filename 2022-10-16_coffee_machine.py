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

is_on = True

def check_resources(order_ingredients):
    """Takes coffe input checks it against to resources to verify if enough ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is Not enough {item}")
            return False
        return True

while is_on:
    # Initial prompt What would you like? (expresso/latte/cappuccino):
    choice = input("What would you like? (espresso/latte/cappuccino):  ").lower()
    if choice == 'report':
        print(generate_report(resources, profit))
    elif choice == 'off':
        is_on = False
    else:
        drink = MENU[choice]
        check_resources(drink['ingredients'])
        # choice == 'espresso':
        # check_resources(resources,choice)
        # print("move ahead")



# TODO: report - prints resources and money inserted

# TODO: prompt to insert money quarters, dimes, nickles, pennies, here is your change, here is your expresso repeat,
#  sorry not enough money and money refunded
# TODO: if resources not enough, sorry, not enough water etc
