# Jordan
# Skomal
# Date: 6/20/23
# Lab 5. This lab shows various operations of the String datatype


def main():
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    length = len(first_name)
    print(f"The length of your first name is {length} characters!")

    length_2 = len(last_name)
    print(f"The length of your last name is {length_2} characters!")

    full_name = f"{first_name} {last_name}"
    print(f"Your full name is {full_name}!")

    n = int(input("Please enter a number: "))
    print(f"Repeating your name {n} times")
    print(f"{first_name}" * n)

    print("Printing your full name with a loop!")
    for ch in full_name:
        print(ch, end="")

    print("\nPrinting the full name using indexing")

    for i in range(len(full_name)):
        print(full_name[i], end="")

    print("\nPrinting the name in reverse order")

    for i in range(len(full_name) - 1, -1, -1):
        print(full_name[i], end="")

    user_name = last_name[0:3] + first_name[0:3]
    print(f"\nYour Username is: {user_name}")


main()
