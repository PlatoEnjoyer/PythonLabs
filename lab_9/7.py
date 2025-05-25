import numpy as np
from sklearn.datasets import load_iris

iris = load_iris()
species_data = iris.target 
species_names = iris.target_names

species_array = np.array([species_names[label] for label in species_data])

unique_values, counts = np.unique(species_array, return_counts=True)

print("Уникальные виды:")
print(unique_values)

print("\nКоличество каждого вида:")
for species, count in zip(unique_values, counts):
    print(f"{species}: {count}")