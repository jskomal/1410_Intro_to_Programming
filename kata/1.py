# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

# Examples:

# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def string_contains(full_str, test_str):
    seen = {}
    has_all_letters = True
    for char in full_str:
        if char not in seen.keys():
            seen[char] = 1
    for input_char in test_str:
        if seen.get(input_char) is None:
            has_all_letters = False
            break
    print(has_all_letters)
    return has_all_letters


string_contains("abc", "bc")
string_contains("abc", "d")
