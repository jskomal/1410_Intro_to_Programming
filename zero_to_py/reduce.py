from functools import reduce


def func(acc, curr):
    print(acc, curr)
    return acc + curr


x = reduce(func, range(10))

print(x)
