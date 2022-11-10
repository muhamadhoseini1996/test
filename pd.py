import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_value = []
y_value = []

index = count()


def animate(i):
    global index
    x_value.append(next(index))
    y_value.append(random.randint(0, 5))
    plt.plot(x_value, y_value)


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()


