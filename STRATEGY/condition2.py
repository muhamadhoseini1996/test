import pandas as pd
import numpy as np
from numpy import random
from utils import ADX, ExponentialMovingAvrage, target, stop_buy, stop_sell, risk_reward_ratio

# ADX indicator
prices_adx = pd.DataFrame(np.random.randint(low=18000, high=23000, size=(100, 5)),
                                        columns=['open', 'high', 'low', 'close', 'values'])
obj_prices = ADX(prices=prices_adx, lookback=14)
obj_prices.update_price(open=22310, high=19963, low=20135, close=25000, values=23555)
plus_new = obj_prices.update_adx_plus()
plus_new = plus_new[len(plus_new)-1]
minus_new = obj_prices.update_adx_minus()
minus_new = minus_new[len(minus_new)-1]
adx_new = obj_prices.update_adx_smooth()


# EMA indicator
prices = pd.Series(random.randint(low=1, high=10, size=10))
close_price = prices[1]
target = target(close_price, 1)
stop_buy = stop_buy(prices, 0.1)
stop_sell = stop_sell(prices, 0.1)
rr_buy = risk_reward_ratio(_target=target, _stop=stop_buy)
rr_sell = risk_reward_ratio(_target=target, _stop=stop_sell)
moving_average_old = ExponentialMovingAvrage(prices, 5)
ema = moving_average_old.update_moving_avrage(close_price)


Trading = False

if (close_price > ema) and (plus_new > minus_new):
    if rr_buy > 1.5:
        if not Trading:
            print('buy')
            Trading = True
        else:
            print('You are trading')
    else:
        print('risk reward ratio is less than 1.5 ')
elif (close_price < ema) and (plus_new < minus_new):
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
