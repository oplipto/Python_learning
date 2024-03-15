my_string = input("Enter anything you want to reverse: ")
my_string_reverse = ""

for char in my_string:
    my_string_reverse = char + my_string_reverse

print(my_string_reverse)