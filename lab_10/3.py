import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn-v0_8')
t = np.linspace(0, 2*np.pi, 1000)
delta = 0

fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.7)
line, = ax.plot([], [], lw=2, color='royalblue')
title = ax.set_title('Соотношение частот: 0:0', fontsize=12)

def init():
    line.set_data([], [])
    return line,

def update(ratio):
    a = 1 
    b = ratio
    
    x = np.sin(a * t + delta)
    y = np.sin(b * t)
    
    line.set_data(x, y)
    title.set_text(f'Соотношение частот: 1:{b:.2f}')
    return line, title

ani = FuncAnimation(fig, update, frames=np.linspace(0, 1, 100),
                    init_func=init, blit=True, interval=50)

plt.show()