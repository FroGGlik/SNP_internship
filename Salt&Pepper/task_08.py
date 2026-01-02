def multiply_numbers(inputs=None):
    string = str(inputs)

    result = 1

    has_digit = any(char.isdigit() for char in string)

    if not has_digit:
        return None

    for char in string:
        if char.isdigit():
            digit = int(char)
            result *= digit

    return result


print(multiply_numbers())
print(multiply_numbers('ss'))
print(multiply_numbers('1234'))
print(multiply_numbers('sssdd34'))
print(multiply_numbers(2.3))
print(multiply_numbers([5, 6, 4]))