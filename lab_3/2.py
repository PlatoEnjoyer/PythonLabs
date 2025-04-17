def swap_min_max(lst):
    if len(lst) == 0:
        return lst
    
    min_val = min(lst)
    max_val = max(lst)
    
    min_index = lst.index(min_val)
    max_index = lst.index(max_val)
    
    lst[min_index], lst[max_index] = lst[max_index], lst[min_index]
    return lst

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(swap_min_max(numbers))