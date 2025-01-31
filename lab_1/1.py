"""
Напишите программу, которая принимает 3 числа, сравнивает между собой и возвращает максимальное и минимальное числа. 
Программа должна также корректно обрабатывать различные варианты равенств чисел. 
Функции min и мах не использовать. Только условный оператор.
"""

numbers = list(map(int, input().split()))

min_max_numbers = [numbers[0], numbers[0]]

def get_max_min_numbers(num, min_max_numbers):
    if num > min_max_numbers[0]:
        min_max_numbers[0] = num
    if num < min_max_numbers[1]:
        min_max_numbers[1] = num
    return

for num in numbers:
    get_max_min_numbers(num, min_max_numbers)


print(f"Максимальное число: {min_max_numbers[0]}, минимальное число: {min_max_numbers[1]}")
