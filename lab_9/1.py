import numpy as np

loaded_matrix = np.loadtxt('matrix_input.txt', delimiter=',', dtype=int)

total_sum = np.sum(loaded_matrix)
max_value = np.max(loaded_matrix)
min_value = np.min(loaded_matrix)

print("Матрица из файла:")
print(loaded_matrix)
print("\nСумма всех элементов:", total_sum)
print("Максимальный элемент:", max_value)
print("Минимальный элемент:", min_value)