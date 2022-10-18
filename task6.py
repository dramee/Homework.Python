test_list = [1, 2, [4, 5], [6, [7, [9, [10]]]], 8]


def flatten(arr):
    new_list = []
    for i in range(len(arr)):
        if isinstance(arr[i], list):
            new_list = [*new_list, *flatten(arr[i])]
        else:
            new_list.append(arr[i])
    return new_list


print(flatten(test_list))
