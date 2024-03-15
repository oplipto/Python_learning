myAge = input("Enter your age: ")
myAge_Int = int(myAge)
myDay = "Wednesday"

price = 20 if myAge_Int >=18 else 10

if myDay == "Wednesday":
    price = price - 2

print("Your ticket price is: ", price)
