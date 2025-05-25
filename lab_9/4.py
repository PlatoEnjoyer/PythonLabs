import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])

zero_before = x[:-1] == 0 
target_elements = x[1:][zero_before]

if len(target_elements) > 0:
    max_val = np.max(target_elements)
else:
    max_val = None

print("Максимальный элемент после нуля:", max_val)