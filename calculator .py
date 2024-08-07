from calculator_art import logo

print(logo)
print("Welcome to the calculator program!")

# Arithmetic operations
def add(num1, num2):
    """Returns the sum of two numbers."""
    return num1 + num2

def sub(num1, num2):
    """Returns the difference of two numbers."""
    return num1 - num2

def mul(num1, num2):
    """Returns the product of two numbers."""
    return num1 * num2

def div(num1, num2):
    """Returns the quotient of two numbers."""
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero!")
    return num1 / num2

symbols = ['+','-','*','/']

def calculate(num1, action, num2):
    if action == '+':
        return add(num1, num2)
    elif action == '-':
        return sub(num1, num2)
    elif action == '*':
        return mul(num1, num2)
    elif action == '/':
        return div(num1, num2)

def calculator ():
    num1 = float(input("What's the first number?: "))
    continue_calculating = True
    while continue_calculating:
        num2 = float(input("What's the second number?: "))
        print("Available operators: ", symbols)
        action = input("Pic an operation?: ")
        result = calculate(num1, action, num2)

        print(f"{num1} {action} {num2} = {result}")

        next_action = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
        if next_action == 'y':
            num1 = result
        else:
            continue_calculating = False
            calculator()

calculator()
   
    



