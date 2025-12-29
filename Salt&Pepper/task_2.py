def coincidence(array=None, band=None) -> list:
    if array is None:
        array = []
    if band is None:
        array = []

    if not isinstance(band, (list, tuple)) or len(band) != 2:
        return []
    
    low, high = band[0], band[1]
    result = []

    for element in array:
        if isinstance(element, (int, float)):
            if low <= element < high:
                result.append(element)
    return result

print(coincidence([1, 2, 3, 4, 5], (3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], (1, 4))) 