def top_three_numbers():
    sequence = input("Введите последовательность чисел: ")
    count_dict = {}
    
    for num in sequence:
        num = int(num)
        count_dict[num] = count_dict.get(num, 0) + 1
    
    sorted_items = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    top_three = dict(sorted_items[:3])
    
    print(top_three)

top_three_numbers()