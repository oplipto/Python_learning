leap_Year = int(input("Enter a year: "))

if (leap_Year % 4 == 0) or (leap_Year % 4 ==0 and leap_Year % 100 != 0):
    print("It's a leap year")
else:
    print("It's NOT a leap year")