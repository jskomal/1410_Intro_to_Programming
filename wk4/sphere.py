from math import pi


def sphere():
    rad = float(input("Please enter the radius of the sphere: "))
    vol = get_volume(rad)
    area = get_area(rad)
    print(
        f"Given a sphere of radius {rad}, the area is {area:.2f}, and the volume is {vol:.2f}."
    )


# 4 pi r squared


def get_volume(radius: float):
    return 4 * pi * (radius**2)


# 4/3 pi r cubed


def get_area(radius: float):
    return 4 / 3 * pi * (radius**3)


sphere()
