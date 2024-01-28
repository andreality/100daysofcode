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

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# recursive function
def calculator(starting_number=None):
    print(logo)
    if starting_number is None:
        starting_number = input("What is the first number?")
    num2 = input("What is the second number?")
    for symbol in operation_dict:
        print(symbol)
    operation = input("Select an operation from the four options above.")
    operation_function = operation_dict[operation]
    result = operation_function(int(starting_number), int(num2))
    print(f"{starting_number} {operation} {num2} = {result}")
    user_continue = input("Would you like to continue with the current value (Y/N)?")
    user_continue = user_continue.lower()
    if user_continue == "y":
        calculator(starting_number=result)
    else:
        print("Starting over!")
        calculator()

calculator()