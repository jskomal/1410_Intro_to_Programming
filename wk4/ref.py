def main():
    obj = {"data": 1}
    print(obj, "init")
    mutate(obj)
    print(obj, "after")


def mutate(entry):
    entry["data"] = 2
    print(entry, "in func")


# def what_string():
#     value = "Hello"
#     print("init", value)
#     mutate_string(value)
#     print("after", value)


# def mutate_string(entry: str):
#     entry += " World"
#     print("in func", entry)


main()
