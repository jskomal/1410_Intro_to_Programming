import copy


def main():
    og = ["Mary", "Sue"]
    list2 = og
    copy_list = copy.copy(og)
    deep_list = copy.deepcopy(og)
    print("Original", og)
    print("Assign", list2)
    print("copy", copy_list)
    print("deepcopy", deep_list)
    og[0] = "Changed"
    print("-----------------------------")
    print('Changed og[0] to "Changed"')
    print("-----------------------------")
    print("Original", og)
    print("Assign", list2)
    print("copy", copy_list)
    print("deepcopy", deep_list)


main()
