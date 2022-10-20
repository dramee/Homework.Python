test_voc = {"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832, "Max": 97832, ((102, 301), 1): 'Aaaa'}

new_voc = {}
for key, value in test_voc.items():
    if value not in new_voc.keys():
        new_voc[value] = key
    elif not(isinstance(new_voc[value], tuple)) or new_voc[value] in test_voc.keys():
        new_voc[value] = (new_voc[value], key)
    else:
        new_voc[value] = (*new_voc[value], key)

print(new_voc)
