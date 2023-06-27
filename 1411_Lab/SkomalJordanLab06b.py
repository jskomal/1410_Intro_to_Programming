# Jordan Skomal | 6/21/2023
# Ceasar Cypher


def ceasar_cypher():
    message = input("Please enter a message: ").strip().casefold()
    key = abs(int(input("Please enter a numerical key: "))) % 26
    # min ord of 'a' is 97 and max ord of 'z' is 122
    # encode the message
    output_cypher = ""
    for ch in message:
        ch_ord = ord(ch)
        # handle space and punctuation
        if ch_ord < 65:
            output_cypher += chr(ch_ord)
            continue
        mod_ord = ch_ord + key
        mod_ord = validate_ord(mod_ord, mode="encode")
        output_cypher += chr(mod_ord)
    print(f"The output string is: {output_cypher}")

    print("Decrypting the text...")

    # decode the message
    output_msg = ""
    for ch in output_cypher:
        ch_ord = ord(ch)
        if ch_ord < 65:
            output_msg += chr(ch_ord)
            continue
        mod_ch = ch_ord - key
        mod_ord = validate_ord(mod_ch, mode="decode")
        output_msg += chr(mod_ord)
    print(f"The original message was: {output_msg}")


def validate_ord(ch_ord: int, mode="encode"):
    lower_bound, upper_bound = 97, 122
    match mode:
        case "encode":
            if ch_ord > upper_bound:
                ch_ord = ch_ord - 123 + 97

        case "decode":
            if ch_ord < lower_bound:
                ch_ord = ch_ord - 97 + 123

        case _:
            raise TypeError("mode must be encode or decode")
    return ch_ord


ceasar_cypher()
