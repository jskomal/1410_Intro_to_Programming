# pizza.py
# calculate the cost / sq inch of a pizza given diameter and price

from math import pi


def sphere(radius):
    return (4 * pi * radius**3) / 3


print(sphere(3))


def price_per_sq_in_pizza(diameter, price):
    radius = diameter / 2
    area = pi * radius**2
    return price / area


print(price_per_sq_in_pizza(10, 15))
