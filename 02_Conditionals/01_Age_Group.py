myAge = input("Enter your age: ")

myAge_Int = int(myAge)

if myAge_Int < 13:
    print("You are a Child")
elif myAge_Int < 20:
    print("You are a Teenager")
elif myAge_Int < 59:
    print("You are an Adult")
else:
    print("You are a Senior Citizen")