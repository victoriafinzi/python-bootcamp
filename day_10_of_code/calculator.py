from replit import clear
from art import logo
print(logo) 

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation = input("Pick an operation from the line above: ")
        last_number = float(input("What's the next number?: "))
        calculation_function = operations[operation]
        answer = calculation_function(first_number, last_number)

        print(f"{first_number} {operation} {last_number} = {answer}")
        
        if input(f"Type 'yes' to continue calculating with {answer} or type 'n' to start a new calculation: ") == 'yes':
            first_number = answer
        else:
            should_continue = False
            calculator()

calculator()
