import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
plt.subplots_adjust(left=0.1, bottom=0.35, right=0.9, top=0.95)

default_amp1, default_freq1 = 1.0, 1.0
default_amp2, default_freq2 = 1.0, 1.0

x = np.linspace(0, 4*np.pi, 1000)

def generate_waves(amp1, freq1, amp2, freq2):
    wave1 = amp1 * np.sin(freq1 * x)
    wave2 = amp2 * np.sin(freq2 * x)
    return wave1, wave2, wave1 + wave2

wave1, wave2, wave_sum = generate_waves(default_amp1, default_freq1, default_amp2, default_freq2)
line1, = ax1.plot(x, wave1, 'b-', lw=2)
line2, = ax2.plot(x, wave2, 'r-', lw=2)
line_sum, = ax3.plot(x, wave_sum, 'g-', lw=2)


for ax, title in zip([ax1, ax2, ax3], ['Волна 1', 'Волна 2', 'Сумма волн']):
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-2.5, 2.5)
    ax.grid(True, linestyle='--', alpha=0.7)
    ax.set_title(title)

axcolor = 'lightgoldenrodyellow'
amp1_ax = plt.axes([0.2, 0.25, 0.65, 0.03], facecolor=axcolor)
freq1_ax = plt.axes([0.2, 0.20, 0.65, 0.03], facecolor=axcolor)
amp2_ax = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor=axcolor)
freq2_ax = plt.axes([0.2, 0.10, 0.65, 0.03], facecolor=axcolor)

amp1_slider = Slider(amp1_ax, 'Амплитуда 1', 0.1, 2.0, valinit=default_amp1)
freq1_slider = Slider(freq1_ax, 'Частота 1', 0.5, 3.0, valinit=default_freq1)
amp2_slider = Slider(amp2_ax, 'Амплитуда 2', 0.1, 2.0, valinit=default_amp2)
freq2_slider = Slider(freq2_ax, 'Частота 2', 0.5, 3.0, valinit=default_freq2)

def update(val):
    amp1 = amp1_slider.val
    freq1 = freq1_slider.val
    amp2 = amp2_slider.val
    freq2 = freq2_slider.val
    
    wave1, wave2, wave_sum = generate_waves(amp1, freq1, amp2, freq2)
    
    line1.set_ydata(wave1)
    line2.set_ydata(wave2)
    line_sum.set_ydata(wave_sum)
    
    max_amp = max(amp1, amp2, np.max(np.abs(wave_sum)))
    for ax in [ax1, ax2, ax3]:
        ax.set_ylim(-max_amp*1.2, max_amp*1.2)
    
    fig.canvas.draw_idle()

amp1_slider.on_changed(update)
freq1_slider.on_changed(update)
amp2_slider.on_changed(update)
freq2_slider.on_changed(update)

plt.show()