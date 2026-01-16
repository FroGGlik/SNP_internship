def max_odd(your_list: list):
    max_odd_num = None

    for element in your_list:
        if isinstance(element, (int, float)):
            if isinstance(element, float):
                if not element.is_integer():
                    continue
                element_int = int(element)
            else:
                element_int = element

            if element_int % 2 != 0:
                if (max_odd_num is None) or (element > max_odd_num):
                    max_odd_num = element

    return max_odd_num


print(max_odd([1, 2, 3, 4, 4]))
print(max_odd([21.0, 2, 3, 4, 4]))
print(max_odd(['ololo', 2, 3, 4, [1, 2], None]))
print(max_odd(['ololo', 'fufufu']))
print(max_odd([2, 2, 4]))