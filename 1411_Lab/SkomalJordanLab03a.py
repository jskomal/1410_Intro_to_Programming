# Lab 3 (pt3)

from math import ceil


def calc_trim(segment_length=12, trim_cost=1.88):
    length = float(input("Please enter the required length in inches: "))
    width = float(input("Please enter the required width in inches: "))
    perimeter = 2 * length + 2 * width
    print(f"The perimeter of your box is {perimeter} inches")
    float_segments_needed = perimeter / segment_length
    int_segments_needed = ceil(float_segments_needed)
    print(f"You will need {int_segments_needed} segments to trim your box")
    int_cost = round(int_segments_needed * trim_cost, 2)
    float_cost = round(float_segments_needed * trim_cost, 2)
    print(f"The cost of your segments is ${int_cost}.")
    print(
        f"You lost ${round(int_cost - float_cost, 2)} because you had to purchase trim in {segment_length} inch sections."
    )


calc_trim()
