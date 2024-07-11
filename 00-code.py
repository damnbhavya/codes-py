import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

plt.rcParams['toolbar'] = 'None'
fig, ax = plt.subplots()

fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.axis('off')

t = np.linspace(0, 2 * np.pi, 1024)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)

line, = ax.plot(x, y, color='red')

fill = None

def animate(i):
    global fill
    t = np.linspace(0, 2 * np.pi * i / 100, 1024)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    line.set_data(x, y)
    if fill:
        fill.remove()
        fill = None
    if i == 99:
        fill = ax.fill_between(x, y, color='red', alpha=1)
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=100, blit=True)

plt.show()