def my_decorator(fn):
    def wrapper():
        print("before func")
        fn()
        print("after func")

    return wrapper


@my_decorator
def my_func():
    print("this is the function")


my_func()
