number = input("Enter a number: ")
number = int(number)
sum_even = 0

for i in range(1, number+1):
    if i % 2 == 0:
        sum_even += i

print("Sum of even number is: ", sum_even)
