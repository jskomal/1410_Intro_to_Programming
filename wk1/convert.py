# convert.py
# A program to convert temperatures from C to F or vice versa via command line
# developed by: Jordan Skomal | June 7, 2023


def convert_temperature():
    try:
        print("Welcome to this temperature convertor")
        print("Choose a mode: ")
        choices = {1, 2}
        mode = int(input("1. C to F \n2. F to C\n"))
        if mode not in choices:
            raise ValueError
        starting_unit = "C" if mode == 1 else "F"
        ending_unit = "F" if mode == 1 else "C"
        temperature = float(
            input(f"Please enter your starting temperature in {starting_unit}: ")
        )
        if mode == 1:
            ending_temp = round(9 / 5 * temperature + 32, 1)
            print(f"The temperature in {ending_unit} is {ending_temp}!")
        else:
            ending_temp = round((temperature - 32) * 5 / 9, 1)
            print(f"The temperature in {ending_unit} is {ending_temp}!")
    except ValueError:
        print("Please enter either 1 or 2 as the option")
        print("Try again!")
        convert_temperature()


convert_temperature()
