def chain(*args):
    for lst in args:
        for el in lst:
            yield el


my_list = [42, 13, 7]

print(list(chain([1, 2, 3], {'a': 1, 'b': 2}, my_list)))
