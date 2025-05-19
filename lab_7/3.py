import json

def add_invoice(json_file: str, new_invoice: dict):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        data['invoices'].append(new_invoice)
        
        output_file = json_file.replace('.json', '_updated.json')
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"Новый счёт добавлен. Результат сохранён в {output_file}")
    
    except Exception as e:
        print(f"Ошибка: {e}")

new_invoice = {
    "id": 3,
    "total": 350.00,
    "items": [
        {
            "name": "item 4",
            "quantity": 3,
            "price": 100.00
        },
        {
            "name": "item 5",
            "quantity": 1,
            "price": 50.00
        }
    ]
}

add_invoice("ex_3.json", new_invoice)