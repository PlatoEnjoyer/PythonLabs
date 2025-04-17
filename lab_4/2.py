def find_key_by_value():
    input_dict = input("Введите словарь (формат 'ключ:значение, ключ:значение'): ").strip()
    
    dictionary = {}
    
    pairs = [pair.strip() for pair in input_dict.split(',') if pair.strip()]
    
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            key = key.strip().strip("'\"")
            value = value.strip().strip("'\"")
            
            try:
                value = int(value)
            except ValueError:
                pass
            
            dictionary[key] = value
    
    search_value = input("Введите значение для поиска: ").strip()
    
    try:
        search_value = int(search_value)
    except ValueError:
        pass
    
    found_keys = [key for key, val in dictionary.items() if val == search_value]
    
    if found_keys:
        print("Найденные ключи:", ", ".join(found_keys))
    else:
        print("Значение не найдено в словаре")

find_key_by_value()
