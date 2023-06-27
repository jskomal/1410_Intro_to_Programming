def main():
    obj = {"data": 1}
    print(obj, "init")
    mutate(obj)
    print(obj, "after")


def mutate(entry):
    entry["data"] = 2
    print(entry, "in func")


def what_string():
    value = "Hello"
    print("init", value)
    val2 = mutate_string(value)
    print("after", value, val2)


def mutate_string(entry: str):
    entry += " World"
    print("in func", entry)
    return entry


def bool_check():
    init = True
    print("init", init)
    init = bool_mutate(init)
    print("after", init)


def bool_mutate(entry):
    entry = False
    print("in func", entry)
    return entry


# main()
# what_string()
bool_check()
