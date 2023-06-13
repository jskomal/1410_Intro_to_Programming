def generator2():
    yield 1
    yield 2


def generator1():
    yield "hello"
    yield from generator2()
    yield from generator2()
    yield "goodbye"


# for result in generator1():
#     print(result)

gen = generator1()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
