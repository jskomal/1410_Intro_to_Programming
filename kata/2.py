# 2. Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. Ensure that each character is used only once.
from itertools import permutations


def find_permutations():
    poss_chars = ["a", "e", "i", "o", "I"]
    big_list = []
    for length in range(len(poss_chars) + 1):
        big_list.append(list(permutations(poss_chars, length)))
    flat_list = [item for sublist in big_list for item in sublist]
    print(flat_list)


find_permutations()
