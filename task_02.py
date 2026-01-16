def coincidence(array=None, band=None) -> list:
    if array is None:
        array = []
    if band is None:
        band = []

    if isinstance(band, range):
        low, high = band.start, band.stop
    elif isinstance(band, (list, tuple)) and len(band) == 2:
        low, high = band[0], band[1]
    else:
        return []

    if low >= high:
        return []

    result = []

    for element in array:
        if isinstance(element, (int, float)):
            if low <= element < high:
                result.append(element)

    return result


print(coincidence([1, 2, 3, 4, 5], range(3, 6)))
print(coincidence())
print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))