list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]

result = {}

for key, value in list_1:
    if key not in result:
        result[key] = [value]
    else:
        result[key].append(value)

print(result)
