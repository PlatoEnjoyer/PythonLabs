import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator, FuncFormatter
from mpl_toolkits.mplot3d import Axes3D

def mse(y_true, y_pred):
    return np.mean((y_true - y_pred)**2) + 1e-8

w1 = np.linspace(-2, 2, 100)
w2 = np.linspace(-2, 2, 100)
W1, W2 = np.meshgrid(w1, w2)

true_w1, true_w2 = 0.7, -0.3
x = np.linspace(-1, 1, 10)
y_true = true_w1 * x + true_w2 * x**2

Z = np.zeros_like(W1)
for i in range(len(w1)):
    for j in range(len(w2)):
        y_pred = W1[i,j] * x + W2[i,j] * x**2
        Z[i,j] = mse(y_true, y_pred)

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(121, projection='3d')
surf1 = ax1.plot_surface(W1, W2, Z, cmap='viridis', alpha=0.8)
ax1.set_title('MSE в линейном масштабе')
ax1.set_xlabel('w1')
ax1.set_ylabel('w2')
ax1.set_zlabel('MSE')
fig.colorbar(surf1, ax=ax1, shrink=0.5, aspect=5)

ax2 = fig.add_subplot(122, projection='3d')

Z_log = np.log10(np.maximum(Z, 1e-10))

surf2 = ax2.plot_surface(W1, W2, Z_log, cmap='plasma', alpha=0.8)
ax2.set_title('MSE в логарифмическом масштабе')
ax2.set_xlabel('w1')
ax2.set_ylabel('w2')
ax2.set_zlabel('log10(MSE)')

ax2.zaxis.set_major_formatter(FuncFormatter(lambda x, _: f'10^{{{x:.1f}}}'))

fig.colorbar(surf2, ax=ax2, shrink=0.5, aspect=5)

plt.tight_layout()
plt.show()