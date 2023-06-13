class MyClass:
    unsafe_list = []

    def __init__(self):
        self.my_list = []

    def add(self, item):
        self.my_list.append(item)

    def unsafe_add(self, item):
        self.unsafe_list.append(item)


shopping = MyClass()
shopping.add("pants")
shopping.unsafe_add("shoes")

grocery = MyClass()
grocery.add("veggies")
grocery.unsafe_add("salad")

print(shopping.my_list)
print(grocery.my_list)
print(shopping.unsafe_list)
print(grocery.unsafe_list)

print(hasattr(shopping, "my_list"))
print(getattr(shopping, "my_list"))
