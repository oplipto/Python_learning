while True:
    print("*************************************")
    print("*        Welcome to the calculator   *")
    print("*************************************")

    my_equation = "1. Add      *\n2. Subtract *\n3. Multiply *\n4. Divide   *\n5. Exit     *"
    print("*************************************")
    print("*         Options                    *")
    print(my_equation)
    print("*************************************")

    my_choice = input("Choose an option: ")

    if my_choice == "1":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {num1 + num2}\n")
        print("*************************************")

    elif my_choice == "2":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The difference of {num1} and {num2} is {num1 - num2}\n")
        print("*************************************")

    elif my_choice == "3":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The product of {num1} and {num2} is {num1 * num2}\n")
        print("*************************************")

    elif my_choice == "4":
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print(f"The quotient of {num1} and {num2} is {num1 / num2}\n")
        print("*************************************")

    elif my_choice == "5":
        print("Goodbye!\n")
        print("*************************************")
        break
