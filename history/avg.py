import matplotlib.pyplot as plt

from numpy import random
from history.utils import moving_average

size, step = 100, 25
price = random.randint(low=18000, high=25000, size=(size,))
Time = list(range(size))


plt.plot(Time, price)
plt.plot(Time, moving_average(price_list=price, step=step, size=size))
plt.show()

print('price = ', list(price))
print('output = ', moving_average(price_list=price, step=step, size=size))

