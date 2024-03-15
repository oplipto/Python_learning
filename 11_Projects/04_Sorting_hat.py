Gryffindor_Points = 0
Ravenclaw_Points = 0
Hufflepuff_Points = 0
Slytherin_Points = 0

print("Welcome to Hogwarts! I am the Sorting Hat.")
print("I will ask you a few questions to determine which house you belong to.")

# Question 1
print("\nQ1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
answer1 = int(input("Enter your choice: "))

if answer1 == 1:
    Gryffindor_Points += 1
    Ravenclaw_Points += 1
elif answer1 == 2:
    Hufflepuff_Points += 1
    Slytherin_Points += 1
else:
    print("Invalid choice")

# Question 2
print("\nQ2) Q2) When I’m dead, I want people to remember me as: ")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")
answer2 = int(input("Enter your choice: "))

if answer2 == 1:
    Hufflepuff_Points += 1
elif answer2 == 2:
    Slytherin_Points += 1
elif answer2 == 3:
    Ravenclaw_Points += 1
elif answer2 == 4:
    Gryffindor_Points += 1

else:
    print("Invalid choice")

# Question 3
print("\nQ3) Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")
answer3 = int(input("Enter your choice: "))

if answer3 == 1:
    Slytherin_Points += 1
elif answer3 == 2:
    Hufflepuff_Points += 1
elif answer3 == 3:
    Ravenclaw_Points += 1
elif answer3 == 4:
    Gryffindor_Points += 1
else:
    print("Invalid choice")


max_points = max(Gryffindor_Points, Ravenclaw_Points, Hufflepuff_Points, Slytherin_Points)

if max_points == Gryffindor_Points:
    print("\nCongratulations! You belong to Gryffindor House.")
elif max_points == Ravenclaw_Points:
    print("\nCongratulations! You belong to Ravenclaw House.")
elif max_points == Hufflepuff_Points:
    print("\nCongratulations! You belong to Hufflepuff House.")
elif max_points == Slytherin_Points:
    print("\nCongratulations! You belong to Slytherin House.")
else:
    print("Invalid choice")

