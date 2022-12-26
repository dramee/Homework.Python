def cycle(lst):
    while True:
        yield from lst


def take(seq, n):
    res = []
    for i in range(n):
        try:
            res.append(next(seq))
        except StopIteration:
            break
    return res


a = [1, 2, 3]

print(take(cycle(a), 10))
