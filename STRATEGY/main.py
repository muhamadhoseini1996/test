import pandas as pd

from utils import *
from numpy import random


prices = pd.Series(random.randint(low=1, high=10, size=10))
print('pricessss', prices)

simple_moving_avrage = ExponentialMovingAvrage(prices, 5)
t = simple_moving_avrage.update_moving_avrage(22)
# print(simple_moving_avrage.length())
# print(simple_moving_avrage.last_avrage())
#

# print(simple_moving_avrage.get_last_moving_avrage())


# result2 = cumulative_moving_average(prices, 2)
# result3 = exponential_moving_average(prices, 2)

# print(f'simple_moving_avrage \n{result1} \n=======================')
# print(f'cumulative_moving_average \n{result2} \n=======================')
# print(f'exponential_moving_average \n{result3} \n=======================')
