myPet = input("What is your pet? ")
myPet_Age = int(input("What is your pet's age? "))


if myPet == "dog" and myPet_Age < 2:
    print("I recommend Pedigree")
elif myPet == "dog" and myPet_Age > 5:
    print("I recommend Royal Canin")
elif myPet == "cat" and myPet_Age < 2:
    print("I recommend Whiskas") 
elif myPet == "cat" and myPet_Age > 5:
    print("I recommend Cat Chow")
else:
    print("I don't have a recommendation for that pet")
