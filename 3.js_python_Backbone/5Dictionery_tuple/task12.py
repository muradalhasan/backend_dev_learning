dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], 'c': [4, 5, 6, 7]}

total_items = 0

for value_list in dict_1.values():
    for item in value_list:
        total_items += 1

print(total_items)
