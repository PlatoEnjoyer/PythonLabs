def greater_than_previous(lst):
    result = []
    for i in range(1, len(lst)):
        if lst[i] > lst[i-1]:
            result.append(lst[i])
    return result


numbers = [1, 5, 2, 4, 3, 6]
print(greater_than_previous(numbers))