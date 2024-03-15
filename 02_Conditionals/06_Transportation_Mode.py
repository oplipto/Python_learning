myDistance = input("Enter the distance you want to travel: ")

if int(myDistance) < 3:
    print("Walk")
elif int(myDistance) < 100:
    print("Bike")
elif int(myDistance) <= 150:
    print("Car")
else:
    print("Take a bus or train")