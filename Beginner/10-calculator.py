import os
from art import calc_logo

def add(n1, n2):
    """Adding two numbers"""
    return n1 + n2

def subtract(n1, n2):
    """Subtractind n2 from n1"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    '''Dividing n1 by n2'''
    return n1 / n2


actions = {'+': add,
           '-': subtract,
           '*': multiply,
           '/': divide,
}

def calculator():
    print(calc_logo)
    num1 = float(input("What\'s the first number?: "))
    next_step = 'y'
    while next_step == 'y':    
        for item in actions:
            print(item)
        action = input('Pick an operator:')
        if action not in actions.keys():
            print("Incorrect operator")
            continue
        else:            
            num2 = float(input("What\'s the second number?: "))
            result = actions[action](num1, num2)
        print(f'{float(num1)} {action} {float(num2)} = {result}')
        next_step = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:  ").lower()
        num1 = result
    else:
        os.system("clear")
        calculator()


calculator()