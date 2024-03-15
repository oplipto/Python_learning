# print("BANK OF PYTHON!")

# pin = int(input("Enter your 4-digit PIN: "))

# while pin != 1234:
#     pin = int(input(print("Invalid PIN. Try again.")))

# if pin == 1234:
#     print("PIN accepted. You may proceed.")
# else:
#     print("Too many attempts. Account locked.")


print("BANK OF PYTHON!")

pin = int(input("Enter your 4-digit PIN: "))

while pin != 1234:
    pin = int(input("Invalid PIN. Try again: "))

if pin == 1234:
    print("PIN accepted. You may proceed.")
