import numpy as np

def rle_encode(x):
    if len(x) == 0:
        return (np.array([], dtype=x.dtype), np.array([], dtype=int))
    
    change_indices = np.where(x[:-1] != x[1:])[0] + 1
    indices = np.concatenate(([0], change_indices, [len(x)]))
    counts = np.diff(indices)
    values = x[indices[:-1]]
    return (values, counts)

x = np.array([2, 2, 2, 3, 3, 3, 5])
values, counts = rle_encode(x)

print("Исходный вектор:", x)
print("Закодированные значения:", values)
print("Количество повторений:", counts)