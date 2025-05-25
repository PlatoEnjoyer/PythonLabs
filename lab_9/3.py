import numpy as np

mean = 0 
std = 1  
data = np.random.normal(mean, std, size=(10, 4))

min_val = np.min(data)
max_val = np.max(data)
mean_val = np.mean(data)
std_val = np.std(data)

first_5_rows = data[:5]

print("Сгенерированный массив:\n", data)
print("\nМинимальное значение:", min_val)
print("Максимальное значение:", max_val)
print("Среднее значение:", mean_val)
print("Стандартное отклонение:", std_val)
print("\nПервые 5 строк:\n", first_5_rows)