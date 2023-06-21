def main():
    print("This program calculates the average word length in a given sentence!")
    sentence = input("Please enter a sentence: ").strip()

    space_count = 1
    char_count = 0
    for ch in sentence:
        ch_ord = ord(ch)
        if ch_ord == 32:
            space_count += 1
            continue
        elif ch_ord < 65:
            continue
        else:
            char_count += 1

    print(f"The average word is {char_count//space_count} characters long!")


main()
