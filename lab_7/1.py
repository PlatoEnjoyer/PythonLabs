import json
from jsonschema import validate, ValidationError

def validate_movies(json_file: str, schema_file: str = "schema.json"):
    try:
        with open(json_file, "r") as f:
            data = json.load(f)
        with open(schema_file, "r") as f:
            schema = json.load(f)
        validate(instance=data, schema=schema)
        print(f"{json_file} валиден по схеме.")
    except ValidationError as e:
        print(f"Ошибка валидации в {json_file}:")
        print(f"Поле: {e.json_path}")
        print(f"Ошибка: {e.message}")
    except json.JSONDecodeError:
        print(f"{json_file} не является корректным JSON.")


validate_movies("ex_1.json")
validate_movies("ex_1_invalid.json")