def my_generator():
    yield 100
    yield 200
    yield 300


gen = my_generator()

print(gen)

# print(next(gen))
# print(next(gen))
# print(next(gen))

# if you do another next it will error

for i in my_generator():
    pass
