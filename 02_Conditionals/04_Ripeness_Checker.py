Fruit = "Banana"

Green = "Unripe"
Yellow = "Ripe"
Brown = "Overripe"

myChoice = input("What Color of Your Banana? : ")

if myChoice == "Green":
    print("Your Banana is Unripe")
elif myChoice == "Yellow":
    print("Your Banana is Ripe")
elif myChoice == "Brown":
    print("Your Banana is Overripe")
else:
    print("Invalid Color")
    exit()