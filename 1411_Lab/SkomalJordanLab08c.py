# Jordan Skomal | 6/28/23


def findDoubles(num_list):
    return list(map(lambda x: x * 2, num_list))


def main():
    vals = []
    for _ in range(5):
        val = float(input("Please enter a number: "))
        vals.append(val)
    doubled_list = findDoubles(vals)
    print(doubled_list)


main()
