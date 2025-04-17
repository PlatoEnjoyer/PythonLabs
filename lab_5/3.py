children = []
with open('lab_5\input3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        parts = line.strip().split()
        if len(parts) >= 3:
            surname, name, age = parts[0], parts[1], int(parts[2])
            children.append({'surname': surname, 'name': name, 'age': age})

youngest = min(children, key=lambda x: x['age'])
oldest = max(children, key=lambda x: x['age'])

with open('lab_5\output3_min.txt', 'w', encoding='utf-8') as f:
    f.write(f"{youngest['surname']} {youngest['name']} {youngest['age']}")

with open('lab_5\output3_max.txt', 'w', encoding='utf-8') as f:
    f.write(f"{oldest['surname']} {oldest['name']} {oldest['age']}")
