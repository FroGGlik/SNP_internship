def max_odd(your_list: list):
    numbers_list = []

    for element in your_list:
        if isinstance(element, (int, float)):
            numbers_list.append(element)
    
    if numbers_list:
        max_el = numbers_list[0]
    else:
        return None

    for num in numbers_list:
        if num > max_el:
            max_el = num
    
    return max_el



print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))