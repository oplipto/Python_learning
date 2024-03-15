my_input = input("Enter anything: ")

for char in my_input:
    print(char)
    if my_input.count(char) == 1:
        print("Your Charcter is: ", char)
        break