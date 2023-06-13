def calc_factorial(n):
    acc = 1
    for num in range(2, n + 1):
        acc *= num
    return acc


print(calc_factorial(100))
print(type(calc_factorial(100)))
