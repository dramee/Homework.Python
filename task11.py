class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step
        print("HEY")

    def increment(self):
        self.count += self.step


class Singleton:
    instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in Singleton.instances:
            Singleton.instances[cls] = super().__new__(cls, *args, **kwargs)
        else:
            cls.__init__ = lambda *new_args, **new_kwargs: None
        return Singleton.instances[cls]


class SingleCounter(Singleton, Counter):
    pass


c1 = SingleCounter()
c2 = SingleCounter()


print(id(c1) == id(c2))




