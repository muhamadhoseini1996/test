import random
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_values = []
y_values = []

index = count()


def animate(i):
    x_values.append(next(index))
    y_values.append(random.randint(5, 25))
    plt.cla()
    plt.plot(x_values, y_values)
    ani = FuncAnimation(plt.gcf(), animate, 5)


plt.tight_layout()
plt.show()

