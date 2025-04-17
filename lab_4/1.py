def get_value_by_key():
    input_str = input("Введите словарь в формате 'ключ:значение, ключ:значение': ")
    
    dictionary = {}
    
    pairs = [pair.strip() for pair in input_str.split(',')]
    
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            key = key.strip().strip("'\"")
            value = value.strip().strip("'\"")
            dictionary[key] = value
    
    key = input("Введите ключ: ").strip("'\"")
    print(dictionary.get(key, "Ключ не найден"))

get_value_by_key()
