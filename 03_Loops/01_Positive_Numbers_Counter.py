number = [1,2,-3,4,-5,6,7,-8,9,10]

positive_numbers_Count = 0

for num in number:
    if num > 0:
        positive_numbers_Count += 1

print("The number of positive numbers is: ", positive_numbers_Count)