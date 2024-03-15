username = "Croods"

def func():
    # username = "Gru"
    print(username)

print(username)
func()

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(2)
# print(result)

# def func3():
#     global x
#     x = 90

# func3()
# print(x)

# def f1():
#     x = 80
#     def f2():
#         print(x)
#     return f2

# my_result = f1()
# my_result()

def myfunc(num):
    def actual(x):
        return x ** num
    return actual

f = myfunc(4)
g = myfunc(4)

print(f(2))
print(g(4))
