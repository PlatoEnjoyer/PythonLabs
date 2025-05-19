import csv
import os
import random
import argparse
from typing import List, Dict, Union

class CSVProcessor:
    def __init__(self, filename: str):
        self.filename = filename
        self.data = []
        self.headers = []
        self._load_data()

    def _load_data(self, separator=','):
        with open(self.filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=separator)
            self.headers = next(reader)
            self.data = [row for row in reader]

    def show(self, mode='top', n=5, separator=','):
        """Выводит данные в удобном формате"""
        if not self.data:
            print("Нет данных для отображения")
            return
        if mode == 'top':
            rows = self.data[:n]
        elif mode == 'bottom':
            rows = self.data[-n:]
        elif mode == 'random':
            rows = random.sample(self.data, min(n, len(self.data)))
        else:
            print("Неверный режим. Используйте 'top', 'bottom' или 'random'")
            return

        if len(rows) < n:
            print(f"Внимание: в файле только {len(rows)} строк")

        col_widths = [max(len(str(item)) for item in zip(*([self.headers] + rows)))]

        header = " | ".join(f"{h:<{w}}" for h, w in zip(self.headers, col_widths))
        print(header)
        print("-" * len(header))

        for row in rows:
            print(" | ".join(f"{item:<{w}}" for item, w in zip(row, col_widths)))

    def info(self):
        """Выводит статистику о данных"""
        if not self.data:
            print("Нет данных для анализа")
            return

        print(f"Размер данных: {len(self.data)}x{len(self.headers)}")

        print("\nСтатистика по столбцам:")
        for i, header in enumerate(self.headers):
            non_empty = sum(1 for row in self.data if i < len(row) and row[i].strip())
            col_data = [row[i] for row in self.data if i < len(row) and row[i].strip()]
            
            data_type = "string"
            if col_data:
                try:
                    _ = [float(item) for item in col_data]
                    data_type = "float"
                    if all(item.isdigit() for item in col_data):
                        data_type = "int"
                except ValueError:
                    pass
            
            print(f"{header:15} {non_empty:5} {data_type}")

    def del_nan(self):
        """Удаляет строки с пустыми значениями"""
        if not self.data:
            return
        rows_to_keep = []
        for row in self.data:
            if all(cell.strip() for cell in row):
                rows_to_keep.append(row)

        removed = len(self.data) - len(rows_to_keep)
        self.data = rows_to_keep
        print(f"Удалено {removed} строк с пустыми значениями")

    def make_ds(self):
        """Разделяет данные на обучающую и тестовую выборки"""
        if not self.data:
            print("Нет данных для разделения")
            return

        os.makedirs("workdata/Learning", exist_ok=True)
        os.makedirs("workdata/Testing", exist_ok=True)

        random.shuffle(self.data)
        split_idx = int(0.7 * len(self.data))

        with open("workdata/Learning/train.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data[:split_idx])

        with open("workdata/Testing/test.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.headers)
            writer.writerows(self.data[split_idx:])

        print(f"Данные разделены: {split_idx} строк в обучающей выборке, {len(self.data)-split_idx} в тестовой")




parser = argparse.ArgumentParser(description="Обработчик CSV файлов")
parser.add_argument("filename", help="Путь к CSV файлу")
args = parser.parse_args()

processor = CSVProcessor(args.filename)

while True:
    print("\nДоступные команды:")
    print("1. show - Показать данные")
    print("2. info - Показать информацию о данных")
    print("3. delnan - Удалить строки с пустыми значениями")
    print("4. makeds - Создать обучающую и тестовую выборки")
    print("5. exit - Выход")

    choice = input("Введите команду: ").strip().lower()

    if choice == 'show':
        mode = input("Режим отображения (top/bottom/random, по умолчанию top): ").strip().lower() or 'top'
        n = input("Количество строк (по умолчанию 5): ").strip()
        n = int(n) if n.isdigit() else 5
        processor.show(mode, n)
    
    elif choice == 'info':
        processor.info()
    
    elif choice == 'delnan':
        processor.del_nan()
    
    elif choice == 'makeds':
        processor.make_ds()
    
    elif choice in ('exit', 'quit'):
        break
    
    else:
        print("Неизвестная команда")
