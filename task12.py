def cycle(lst):
    while True:
        for i in lst:
            yield i


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
