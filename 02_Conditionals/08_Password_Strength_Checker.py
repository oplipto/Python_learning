myPassword = input("Enter your password: ")

if len(myPassword) < 6:
    print("Your Password is Weak")
elif len(myPassword) <= 10:
    print("Your Password is Medium")
else:
    print("Your Password is Strong")