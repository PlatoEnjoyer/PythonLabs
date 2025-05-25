import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

plt.figure(figsize=(10, 6))
x = np.linspace(-1, 1, 400)
colors = plt.cm.viridis(np.linspace(0, 1, 7))

for n in range(1, 8):
    Pn = legendre(n)
    y = Pn(x)
    line, = plt.plot(x, y, color=colors[n-1], lw=2, label=f'n = {n}')
    
    max_idx = np.argmax(np.abs(y))
    plt.annotate(f'n = {n}', xy=(x[max_idx], y[max_idx]),
                 xytext=(20, 20), textcoords='offset points',
                 bbox=dict(boxstyle='round,pad=0.5', fc='white', alpha=0.8),
                 arrowprops=dict(arrowstyle='->'))

plt.title('Полиномы Лежандра', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('P_n(x)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.legend(loc='upper right')

plt.tight_layout()
plt.show()