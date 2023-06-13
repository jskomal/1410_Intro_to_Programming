# SkomalJordanLab02a.py
# This is lab 2. It takes in a temperature in Fahrenheit and converts it
# to Celsius. It also queries the user for their name.


def main():
    # first, ask the user for their first and last names
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    # now ask them for the temperature they wish to convert
    fahren = int(input("What is the temperature in Fahreneit? "))

    # next we convert using the standard F to C formula
    celsius = (fahren - 32) * (5 / 9)

    # finally, print out the conversion
    print(f"{first_name} {last_name}, the Celcius temperature is {celsius} degrees.")
