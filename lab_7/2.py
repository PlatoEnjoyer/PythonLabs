import json

def extract_users(json_file: str):
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            users = json.load(f)
        
        user_dict = {user["name"]: user["phoneNumber"] for user in users}
        
        print("Список пользователей (имя -> телефон):")
        for name, phone in user_dict.items():
            print(f"{name}: {phone}")
            
        with open("users_phones.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(f"{k}: {v}" for k, v in user_dict.items()))
            
    except Exception as e:
        print(f"Ошибка: {e}")

extract_users("ex_2_formatted.json")