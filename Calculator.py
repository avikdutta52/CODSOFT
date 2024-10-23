def calculator():
    print("Welcome to the simple calculator!")
    
    # Input two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Input the operation
    print("Choose an operation: +, -, *, /")
    operation = input("Enter the operation: ")

    # Perform the operation and display the result
    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation selected. Please choose +, -, *, or /.")
    
calculator()
