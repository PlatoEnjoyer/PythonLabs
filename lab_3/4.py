def count_string_occurrences(strings):
    counts = {}
    for s in strings:
        counts[s] = counts.get(s, 0) + 1
    return ' '.join(map(str, counts.values()))


test1 = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
print(count_string_occurrences(test1))

test2 = ['aaa', 'bbb', 'ccc']
print(count_string_occurrences(test2))

test3 = ['abc', 'abc', 'abc']
print(count_string_occurrences(test3))