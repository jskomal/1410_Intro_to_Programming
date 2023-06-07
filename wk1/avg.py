def main():
    try:
        a, b, c, d, e = map(
            float, input("Enter five numbers separated by only spaces: ").split()
        )
        tot = a + b + c + d + e
        avg = tot / 5
        print(f"your total is {tot} and your average is {avg}")
    except ValueError:
        print("One or more of the provided values is not a number.")
        print("Please try again!")
        main()


main()
