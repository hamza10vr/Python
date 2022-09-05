#Calculator




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
    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)

    continue_calculation = True
    while continue_calculation:
        
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("what's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        yes_or_no = input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit.: ")
        if yes_or_no == 'y':
            num1 = answer
        else:
            continue_calculation = False
            calculator()

calculator()

