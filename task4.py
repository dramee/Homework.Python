test_voc = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Max": 97832}

# test_voc = {}
# l = int(input())
#
# for i in range(l):
#     voc_key, voc_value = input().split()
#     voc_value = int(voc_value)
#     test_voc[voc_key] = voc_value

new_voc = {}
for key, value in test_voc.items():
    if value not in new_voc.keys():
        new_voc[value] = key
    else:
        if isinstance(new_voc[value], tuple):
            new_voc[value] = (*new_voc[value], key)
        else:
            new_voc[value] = (new_voc[value], key)
print(new_voc)


