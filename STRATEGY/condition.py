import pandas as pd
from numpy import random
import numpy

from utils import (SimpleMovingAvrage, ExponentialMovingAvrage, CumulativeMovingAvrage, ADX, plus_di,minus_di, adx)
from utils import (stop_buy, stop_sell, risk_reward_ratio, target)


prices = pd.Series(random.randint(low=1, high=10, size=10))

# simple_moving_avrage = ExponentialMovingAvrage(prices, 5)
# t = simple_moving_avrage.update_moving_avrage(22)

close_price = prices[1]
target = target(close_price, 1)
stop_buy = stop_buy(prices, 0.1)
stop_sell = stop_sell(prices, 0.1)
rr_buy = risk_reward_ratio(_target=target, _stop=stop_buy)
rr_sell = risk_reward_ratio(_target=target, _stop=stop_sell)

moving_average_old = ExponentialMovingAvrage(prices, 5)
ema = moving_average_old.update_moving_avrage(close_price)

# ================================================= ADX PART ========================================================

data_prices = pd.DataFrame(numpy.random.randint(low=19503,
                                                high=26152,
                                                size=(100, 5)),
                                                columns=['open', 'high', 'low', 'close', 'values'])

obj_prices = ADX(prices=prices, lookback=14)
plus = plus_di(prices, obj_prices.get_adx_plus())
minus = minus_di(prices, obj_prices.get_adx_minus())
adx = adx(prices, obj_prices.get_adx_smooth())

plus = plus.dropna()
minus = minus.dropna()
adx = adx.dropna()

plus.tail()
minus.tail()
adx.tail()

test_adx = obj_prices = ADX(prices=prices, lookback=14)


obj_prices.update_price(open=22310, high=19963, low=20135, close=25000, values=23555)

plus_new = obj_prices.update_adx_plus()
minus_new = obj_prices.update_adx_minus()
adx_new = obj_prices.update_adx_smooth()

plus_new = plus_new.dropna()
plus_new.tail()
minus_new = minus_new.dropna()
minus_new.tail()
adx_new = adx_new.dropna()
adx_new.tail()

# =======================================================================================================================
Trading = False

if (close_price > ema) and (data_prices['plus_di'][14] > data_prices['minus_di'][14]):
    if rr_buy > 1.5:
        if not Trading:
            print('buy')
            Trading = True
        else:
            print('You are trading')
    else:
        print('risk reward ratio is less than 1.5 ')
elif (close_price < ema) and (data_prices['plus_di'][14] < data_prices['minus_di'][14]):
    if rr_sell > 1.5:
        if not Trading:
            Trading = True
            print('sell')
        else:
            print('You are trading')
    else:
        print('risk reward ratio is less than 1.5 ')
else:
    print('There are no conditions for Trading currency')
