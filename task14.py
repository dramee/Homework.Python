import functools
def coroutine(func, *args, **kwargs):
    @functools.wraps(func)
    def wrapper():
        new_el = func(*args, **kwargs)
        new_el.send(None)
        return new_el

    return wrapper


@coroutine
def storage():
    values = set()
    was_there = False
    while True:
        val = yield was_there
        was_there = val in values
        if not was_there:
            values.add(val)


st = storage()
print(st.send(42))
print(st.send(42))
