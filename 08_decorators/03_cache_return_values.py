import time

def cache (funct):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = funct(*args)
        return cache[args]
    return wrapper

@cache
def slow_function(a, b):
    time.sleep(4)
    return a + b

print(slow_function(3, 7))
