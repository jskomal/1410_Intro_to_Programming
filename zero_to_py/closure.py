# def make_counter():
#     count = 0

#     def counter():
#         count += 1
#         return count

#     return counter


# my_counter = make_counter()
# print("No nonlocal")
# print(my_counter())
# print(my_counter())
# print(my_counter())
# print("---------------")


def make_nonlocal_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


my_counter2 = make_nonlocal_counter()
print("with nonlocal")
print(my_counter2())
print(my_counter2())
print(my_counter2())
