class Counter:
    def __init__(self, initial_count=0, step=1):
        self.count = initial_count
        self.step = step

    def increment(self):
        self.count += self.step


class Singleton:
    instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__init__(cls, *args, **kwargs)
        return cls.instances[cls]


class SingleCounter(Singleton, Counter):
    pass


c1 = SingleCounter()
c2 = SingleCounter()

print(id(c1) == id(c2))
