x = [n for n in range(10) if n % 2 == 0]

# print(x)

my_dict = {"name": "Jordan", "last": "Skomal"}

num_dict = {0: 0, 8: 64, 2: 4, 4: 16, 6: 36}


y = {key + " string": val for (key, val) in my_dict.items()}

z = {n: num_dict[n] ** 2 for n in num_dict}

a = sum(num_dict.values())

print(a)
