myGrade = input("Enter your Score: ")
myGrade_Int = int(myGrade)
if myGrade_Int >= 101:
    print("Invalid Score")
    exit()

if myGrade_Int >= 90:
    print("You got an A Grade")
elif myGrade_Int >= 80:
    print("You got a B Grade")
elif myGrade_Int >= 70:
    print("You got a C Grade")
elif myGrade_Int >= 60:
    print("You got a D Grade")
else:
    print("You got an F Grade")