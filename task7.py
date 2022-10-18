test_list = [1, 2, [4, 5], [6, [7, [9, [10]]]], 8]


def flatten(arr, depth=float('+inf')):
    new_list = []
    for i in range(len(arr)):
        if isinstance(arr[i], list) and depth:
            new_list = [*new_list, *flatten(arr[i], depth-1)]
        else:
            new_list.append(arr[i])
    return new_list


for i in range(5):
    print(f"{i}: {flatten(test_list, depth=i)}", end="\n")

