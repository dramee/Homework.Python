def specialize(func, *args, **kwargs):
    def newfunc(*args1, **kwargs1):
        return func(*args, *args1, **kwargs, **kwargs1)
    return newfunc



def my_sum(x, y):
    return x+y


# plus_one = specialize(my_sum, 1)

# just_two = specialize(my_sum, 1, 1)

# print(plus_one(10))

# print(just_two())
