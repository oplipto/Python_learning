import math

def radius_area_circumference(radius):
    area = math.pi * radius **2
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = radius_area_circumference(10)

a = round(a, 2)
c = round(c, 2)

print("Area: ", a, "Circumference: ", c)