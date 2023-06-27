from math import pi


def circle_area(radius):
    return pi * (radius**2)


def main():
    rad = float(input("Please enter a radius: "))
    area = circle_area(rad)
    print(f"The area of your circle is {area:.2f}")


main()
