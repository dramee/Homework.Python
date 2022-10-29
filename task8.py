import functools


def deprecated(f=None, since=None, will_be_removed=None):

    if f is None:
        return functools.partial(deprecated, since=since, will_be_removed=will_be_removed)

    @functools.wraps(f)
    def inner(*args, **kwargs):
        if since is None and will_be_removed is None:
            print(f"Warning: function {f.__name__} is deprecated."
                  f" It will be removed in future versions.")
        elif since is None:
            print(f"Warning: function {f.__name__} is deprecated. It will be removed in version {will_be_removed}.")
        elif will_be_removed is None:
            print(f"Warning: function {f.__name__} is deprecated since version {since}."
                  f" It will be removed in future versions.")
        else:
            print(f"Warning: function {f.__name__} is deprecated since version {since}."
                  f" It will be removed in version {will_be_removed}.")
        ret = f(*args, **kwargs)
        return ret
    return inner


@deprecated(since=2, will_be_removed=3)
def my_sum(x, y):
    return x + y


print(my_sum(10, 2))
