while True:
    print("Welcome to Simple Calculator:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    print("5: Exit")

    my_choice = int(input("Enter your choice: "))

    if my_choice in [1, 2, 3, 4]:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if my_choice == 1:
            result = a + b
            operation = "Addition"
        elif my_choice == 2:
            result = a - b
            operation = "Subtraction"
        elif my_choice == 3:
            result = a * b
            operation = "Multiplication"
        elif my_choice == 4:
            if b == 0:
                print("Error: Division by zero!")
                continue
            result = a / b
            operation = "Division"

        print(f"\n{operation} Result:")
        print(f"{a} {operation} {b} = {result}\n")

    elif my_choice == 5:
        print("Exiting the calculator. Goodbye!")
        break

    else:
        print("Invalid choice. Please select a valid option.\n")
