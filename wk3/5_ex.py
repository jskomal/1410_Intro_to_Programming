from math import pi


def grade_from_score(score):
    score = str(score)
    key = "5-A, 4-B, 3-C, 2-D, 1-F, 0-F"
    key_list = key.split(", ")
    key_dict = {}
    for entry in key_list:
        if entry[0] not in key_dict:
            key_dict[entry[0]] = entry[2]
    print(key_dict[score])


# grade_from_score("1")
# grade_from_score(1)
# grade_from_score(2)
# grade_from_score(3)
# grade_from_score(4)
# grade_from_score(5)


def grade_from_score_2(score):
    score = int(score)
    key = "90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F"
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    elif score >= 60:
        print("D")
    elif score < 60:
        print("F")
    else:
        raise ValueError("How?")


# grade_from_score_2(1)
# grade_from_score_2(100)
# grade_from_score_2(79)
# grade_from_score_2(50)


def acronym_maker(string: str):
    in_list = string.split(" ")
    result = ""
    for word in in_list:
        result += word[0].capitalize()
    print(result)


# acronym_maker("Hello World")


def ord_destroyer(name: str):
    acc = 0
    name = name.casefold()
    for ch in name:
        if ord(ch) - 96 < 0:
            continue
        acc += ord(ch) - 96
    print(acc)


# ord_destroyer("Jordan")
# ord_destroyer("Zelle")


def format_prac(num):
    formatted = "{0:0.20f}".format(pi)
    print(f"the number is {formatted}")
    print("{0}={1:.2f}".format("pi", 3.14159))
    print(eval("09"))


format_prac(pi)
