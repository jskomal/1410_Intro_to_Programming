def greet(name, /, title, *, punc):
    print(f"Hello {name}, {title}{punc}")


greet("Jordan", "Esq", punc="!")
