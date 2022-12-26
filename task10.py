class LRUCache:

    cache = {}
    add_time = {}
    count = 0

    def __init__(self, capacity=16):
        self.cap = capacity
        self.cache = {}
        self.add_time = {}
        self.count = 0

    def put(self, key, value):
        if key not in LRUCache.cache.keys():
            if len(LRUCache.cache) >= self.cap:
                # print("=" * 100)
                # print("DELETE PROCESS")
                # print("=" * 100)
                key_to_del = min(LRUCache.cache.keys(), key=lambda k: LRUCache.add_time[k])
                LRUCache.cache.pop(key_to_del)
                LRUCache.add_time.pop(key_to_del)
            LRUCache.cache[key] = value
            LRUCache.add_time[key] = LRUCache.count

    def get(self, key):
        LRUCache.count += 1
        LRUCache.add_time[key] += LRUCache.count
        return LRUCache.cache[key]


# c = LRUCache()
#
# for i in range(-6, 6):
#     x = i ** 2
#     c.put(i, x)
# print(LRUCache.cache, end=("\n" * 2))
#
# for j in range(-10, 10):
#     if j in LRUCache.cache.keys():
#         print("=" * 100)
#         print(c.get(j))
#         print("=" * 100)
#     else:
#         x = j ** 2
#         c.put(j, x)
#     print(LRUCache.cache, LRUCache.add_time, sep=" \n", end=("\n" * 2))