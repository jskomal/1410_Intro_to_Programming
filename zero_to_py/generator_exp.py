numbers = range(10)

even_numbers = (num for num in numbers if num % 2 == 0)

squared_numbers = (n**2 for n in numbers)

print(list(numbers))
print(list(even_numbers))
print(list(squared_numbers))
