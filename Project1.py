# Smart Calculator

name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to the Smart Calculator.")
def smart_calculator():
        
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    operation = input("Enter the operation (+,-,*,/,**,%): ")

    if operation == "+":
        result = x + y 
    elif operation == "-":
        result = x -y 
    elif operation == "*":
        result = x * y
    elif operation == '/':
        if y != 0:
            result = x/y
        else:
            return "Error: Division by zero is not allowed."
    elif operation == '^':
        result = x**y
    elif operation == '%':
        if y != 0:
            result = x%y
    else:
        return "Error: Invalid operation."
    
    return f'{x} {operation} {y} = {result}'

print(smart_calculator())