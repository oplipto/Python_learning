my_Order = "1: Small, 2: Medium, 3: Large"

print(my_Order)

size = input("What size would you like? (1/2/3): ")

extra_shot = True

if extra_shot:
    print("You have selected extra shot")
else:
    print("You have not selected extra shot")


if size == "1":
    print("You have selected Small")
elif size == "2":
    print("You have selected Medium")
elif size == "3":
    print("You have selected Large")
else:
    print("Invalid choice. Please select from 1, 2 or 3")
