import functools


def deprecated(f=None, since=None, will_be_removed=None):

    if f is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    @functools.wraps(f)
    def inner(*args, **kwargs):
        print(f"Warning: function {f.__name__} is deprecated", end="")
        if not(since is None):
            print(f" since version {since}", end="")
        print(". It will be removed in", end=" ")
        if not(will_be_removed is None):
            print(f"version {will_be_removed}.")
        else:
            print("future versions.")
        ret = f(*args, **kwargs)
        return ret
    return inner


@deprecated(since=2.1231)
def my_sum(x, y):
    return x + y


print(my_sum(10, 2))
