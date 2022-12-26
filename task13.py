def chain(*args):
    for lst in args:
        yield from lst


my_list = [42, 13, 7]

print(list(chain([1, 2, 3], {'a': 1, 'b': 2}, my_list)))
