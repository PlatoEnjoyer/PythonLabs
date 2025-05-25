import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000) 
delta = np.pi / 2
ratios = [(3, 2), (3, 4), (5, 4), (5, 6)]
titles = ['Соотношение 3:2', 'Соотношение 3:4', 'Соотношение 5:4', 'Соотношение 5:6']

fig, axes = plt.subplots(2, 2, figsize=(10, 8))
fig.suptitle('Фигуры Лиссажу для разных соотношений частот', fontsize=14)

for i, ((a, b), ax) in enumerate(zip(ratios, axes.flatten())):
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    
    ax.plot(x, y, color='royalblue', linewidth=2)
    ax.set_title(titles[i], fontsize=10)
    ax.set_xlabel('X: sin({}t + π/2)'.format(a))
    ax.set_ylabel('Y: sin({}t)'.format(b))
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.set_aspect('equal')

plt.tight_layout()
plt.show()