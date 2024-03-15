def print_kwargs(**kwargs):
   for key, value in kwargs.items():
         print(f"{key}: {value}")

print_kwargs(name="John", age=25, city="New York")
print_kwargs(name="Jane", age=30, city="San Francisco", email="IDK@Gmail.com")
