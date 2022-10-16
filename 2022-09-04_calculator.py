#Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)


def add( n1, n2):
    """ adds n1 and n2 """
    return n1 + n2

def subtract( n1, n2):
    """ adds n1 and n2 """
    return n1 - n2

def multiply( n1, n2):
    """ adds n1 and n2 """
    return n1 * n2

def divide( n1, n2):
    """ adds n1 and n2 """
    return n1 / n2

operations = {
    '+': add, 
    '-': subtract, 
    '*': multiply, 
    '/': divide
    }

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_calculation = True
    while continue_calculation:
        
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("what's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        options = input(f"Type 'y' to continue calculating with {answer} or type 'new' to start a new calculation or type 'n' to exit.: ")
        if options == 'y':
            num1 = answer
        elif options == 'new':
            calculator()
        elif options == 'n':
            continue_calculation = False


calculator()

