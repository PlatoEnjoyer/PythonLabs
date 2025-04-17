def count_string_occurrences():
    strings = eval(input("Введите список строк: "))
    counts = {}
    
    for s in strings:
        counts[s] = counts.get(s, 0) + 1
    
    result = counts.values()
    print(' '.join(map(str, result)))

count_string_occurrences()