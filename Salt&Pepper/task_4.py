def sort_list(num_list):
    if not num_list:
        return []
    
    max_val = max(num_list)
    min_val = min(num_list)

    for i in range(len(num_list)):
        if num_list[i] == min_val:
            num_list[i] = max_val
        elif num_list[i] == max_val:
            num_list[i] = min_val

    num_list.append(min_val)

    return num_list


print(sort_list([]))
print(sort_list([2, 4, 6, 8]))
print(sort_list([1]))
print(sort_list([1, 2, 1, 3]))