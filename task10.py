class LRUCache:

    cache = {}
    add_time = {}
    count = 0

    def __init__(self, capacity=16):
        self.cap = capacity

    def put(self, key, value):
        if key not in LRUCache.cache.keys():
            if len(LRUCache.cache) >= self.cap:
                # print("=" * 100)
                # print("DELETE PROCESS")
                # print("=" * 100)
                m = -1
                key_to_del = None
                for old_key in LRUCache.cache.keys():
                    diff = LRUCache.count - LRUCache.add_time[old_key]
                    if diff > m:
                        m = diff
                        key_to_del = old_key
                LRUCache.cache.pop(key_to_del)
                LRUCache.add_time.pop(key_to_del)
            LRUCache.cache[key] = value
            LRUCache.add_time[key] = 0

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