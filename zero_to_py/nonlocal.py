def outer():
    nonlocal_var = "Hello"

    def inner():
        nonlocal nonlocal_var
        print("first", nonlocal_var)
        nonlocal_var = "Changed"
        print("second", nonlocal_var)

    inner()
    print("third", nonlocal_var)


outer()


def leak():
    greeting = "Hello"

    def inner():
        greeting = "Hi"
        print("inner", greeting)

    inner()
    print("outer", greeting)


leak()
