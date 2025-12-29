def connect_dicts(dict1, dict2):
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        primary, secondary = dict1, dict2

    elif sum2 > sum1:
        primary, secondary = dict2, dict1

    else:
        primary, secondary = dict2, dict1

    combined_keys = list(primary.keys())
    for key in secondary:
        if key not in combined_keys:
            combined_keys.append(key)

    result = {}
    for key in combined_keys:
        val = primary.get(key, secondary.get(key))
        if val > 10:
            result[key] = val

    return dict(sorted(result.items(), key=lambda item: item[1]))


print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }))
print(connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }))
print(connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 }))