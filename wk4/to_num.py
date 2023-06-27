from typing import List

data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


def to_nums(strs: List[str]):
    result = map(int, strs)
    for entry in result:
        print(entry)


to_nums(data)
