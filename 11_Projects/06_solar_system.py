
from math import pi
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)

if random_planet == 'Earth':
  r = 6371

elif random_planet == 'Mars':
    r = 3389

elif random_planet == 'Mercury':
    r = 2439

elif random_planet == 'Venus':
    r = 6052

elif random_planet == 'Saturn':
    r = 60268

else:
    print("Oops! Something went wrong.")

area = 4 * pi * r ** 2

print(f"The radius of {random_planet} is {area:.2f} km.")
