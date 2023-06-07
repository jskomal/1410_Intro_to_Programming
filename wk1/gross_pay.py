def main():
    print("Hello, Let's calculate your payday!!!")
    hours = float(input("Please enter your hours worked: "))
    rate = float(input("Please enter your pay rate in dollars per hour: "))
    pay = hours * rate
    print(f"Your estimated pay for this period is {pay}")


main()
