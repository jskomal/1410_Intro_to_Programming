# Your first name
# Your last name
# Date: The current date
# Description: This program shows techniques of defining function,
# parameter passing    and function invocation.


# fahrenToCel function
# parameter: A temperature value in Fahrenheit
# returns equivalent temperature in Celsius
def fahrenToCel(fahren):
    result = (fahren - 32) * (5.0 / 9.0)
    return result


# fahrenToCelList function
# parameter: a list of temperature values in Fahrenheit
# coverts the list to equivalent temperatures in Celsius
# If you pass a list as an argument, this will change the value
# in calling function
def fahrenToCelList(fahrenList):
    for i in range(len(fahrenList)):
        fahren = fahrenList[i]
        celsius = (fahren - 32) * (5.0 / 9.0)
        fahrenList[i] = round(celsius, 2)


# main function
def main():
    fval = float(input("Please enter the temperature in Fahrenheit: "))
    # call the function fahrenToCel
    cval = fahrenToCel(fval)
    print("Equivalent temperature in Celcius is {0:0.2f} ".format(cval))

    fahrenheitList = []
    # Take 5 temperature values as inputs and store them in fahrenheitList
    for i in range(5):
        fahren = float(input("Enter temperature in Fahrenheit: "))
        fahrenheitList.append(fahren)

    # call the function fahrenToCelList
    fahrenToCelList(fahrenheitList)
    print("The converted temperature list")
    print(fahrenheitList)


main()
