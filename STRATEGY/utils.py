import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt


prices = pd.DataFrame(np.random.randint(low=18000, high=23000, size=(100, 5)),
                                        columns=['open', 'high', 'low', 'close', 'values'])

class SimpleMovingAvrage:
    """
        #TODO: write docstring for this data type
    """

    def __init__(self, prices, windows_size):
        self.prices = self.__series(prices)
        self.update_avrage_frame = list(prices[-windows_size:])
        self.windows_size = windows_size
        self.avrages = self.moving_avrage(prices,
                                          windows_size)
        self.avrages.reset_index(drop=True, inplace=True)

    def moving_avrage(self, data_frame, window_size):
        data_frame = self.__series(data_frame)
        result = data_frame.rolling(window_size).mean()
        result.dropna(inplace=True)
        return result

    def update_moving_avrage(self, new_price):
        self.update_avrage_frame.pop(0)
        self.update_avrage_frame.append(new_price)
        result = np.mean(self.update_avrage_frame)
        self.__add_new_avrage(result)
        return result

    def get_avrage(self, index=None):
        if index == None:
            return list(self.avrages)
        elif index < self.length():
            return self.avrages[index]
        return None

    def last_avrage(self):
        return self.get_avrage(self.length()-1)

    def length(self):
        return len(self.avrages)

    def __add_new_avrage(self, new_avrage):
        # TODO: check size of self.avrage and append new value
        self.avrages[self.length()] = new_avrage

    def __series(self, prices):
        # TODO check input this pandas serize
        return prices

    def __getitem__(self, index):
        try:
            return self.get_avrage(index)
        except IndexError:
            return None

    def __str__(self):
        return str(self.get_avrage())


class ExponentialMovingAvrage:
    """
        #TODO: write docstring for this data type
    """

    def __init__(self, prices, windows_size):
        self.prices = self.__series(prices)
        self.update_avrage_frame = list(prices[-windows_size:])
        self.windows_size = windows_size
        self.avrages = self.moving_avrage(prices,
                                          windows_size)
        self.avrages.reset_index(drop=True, inplace=True)

    def moving_avrage(self, data_frame, window_size):
        data_frame = self.__series(data_frame)
        result = data_frame.ewm(span=window_size).mean()
        result.dropna(inplace=True)
        return result

    def update_moving_avrage(self, new_price):
        self.update_avrage_frame.pop(0)
        self.update_avrage_frame.append(new_price)
        result = np.mean(self.update_avrage_frame)
        self.__add_new_avrage(result)
        return result

    def get_avrage(self, index=None):
        if index == None:
            return list(self.avrages)
        elif index < self.length():
            return self.avrages[index]
        return None

    def last_avrage(self):
        return self.get_avrage(self.length()-1)

    def length(self):
        return len(self.avrages)

    def __add_new_avrage(self, new_avrage):
        # TODO: check size of self.avrage and append new value
        self.avrages[self.length()] = new_avrage

    def __series(self, prices):
        # TODO check input this pandas serize
        return prices

    def __getitem__(self, index):
        try:
            return self.get_avrage(index)
        except IndexError:
            return None

    def __str__(self):
        return str(self.get_avrage())


class CumulativeMovingAvrage:

    """
        #TODO: write docstring for this data type
    """

    def __init__(self, prices, windows_size):
        self.prices = self.__series(prices)
        self.update_avrage_frame = list(prices[-windows_size:])
        self.windows_size = windows_size
        self.avrages = self.moving_avrage(prices,
                                          windows_size)
        self.avrages.reset_index(drop=True, inplace=True)

    def moving_avrage(self, data_frame, window_size):
        data_frame = self.__series(data_frame)
        result = data_frame.expanding(window_size).mean()
        result.dropna(inplace=True)
        return result

    def update_moving_avrage(self, new_price):
        self.update_avrage_frame.pop(0)
        self.update_avrage_frame.append(new_price)
        result = np.mean(self.update_avrage_frame)
        self.__add_new_avrage(result)
        return result

    def get_avrage(self, index=None):
        if index == None:
            return list(self.avrages)
        elif index < self.length():
            return self.avrages[index]
        return None

    def last_avrage(self):
        return self.get_avrage(self.length()-1)

    def length(self):
        return len(self.avrages)

    def __add_new_avrage(self, new_avrage):
        # TODO: check size of self.avrage and append new value
        self.avrages[self.length()] = new_avrage

    def __series(self, prices):
        # TODO check input this pandas serize
        return prices

    def __getitem__(self, index):
        try:
            return self.get_avrage(index)
        except IndexError:
            return None

    def __str__(self):
        return str(self.get_avrage())


class ADX:
    """
        #TODO: write docstring for this data type
    """

    def __init__(self, prices, lookback):
        self.prices = prices
        self.high = prices['high']
        self.low = prices['low']
        self.close = prices['close']
        self.lookback = lookback
        self.tr1 = pd.DataFrame(self.high - self.low)
        self.tr2 = pd.DataFrame(abs(self.high - self.close.shift(1)))
        self.tr3 = pd.DataFrame(abs(self.low - self.close.shift(1)))
        self.frames = [self.tr1, self.tr2, self.tr3]
        self.tr = pd.concat(self.frames, axis=1, join='inner').max(axis=1)
        self.atr = self.tr.rolling(self.lookback).mean()

    def update_price(self, open, high, low, close, values):
        new_price = pd.Series([open, high, low, close, values])
        df = pd.DataFrame([list(new_price)], columns=["open", "high", "low", "close", "values"])
        self.prices = self.prices.append(df, ignore_index=True)
        self.prices.reset_index(level=None, drop=False, inplace=False, col_level=0, col_fill='')

    def get_adx_plus(self):
        plus_dm = self.high.diff()
        plus_dm[plus_dm < 0] = 0
        plus_di = 100 * \
            (plus_dm.ewm(alpha=1 / self.lookback).mean() / self.atr)
        return plus_di

    def update_adx_plus(self):
        tr1 = pd.DataFrame(self.prices['high'] - self.prices['low'])
        tr2 = pd.DataFrame(abs(self.prices['high'] - self.prices['close'].shift(1)))
        tr3 = pd.DataFrame(abs(self.prices['low'] - self.prices['close'].shift(1)))
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis=1, join='inner').max(axis=1)
        atr = tr.rolling(self.lookback).mean()

        plus_dm = self.prices['high'].diff()
        plus_dm[plus_dm < 0] = 0
        plus_di = 100 * \
            (plus_dm.ewm(alpha=1 / self.lookback).mean() / atr)
        return plus_di

    def get_plus_di(self):
        self.prices['plus_di'] = pd.DataFrame(self.get_adx_plus()).rename(columns={0: 'plus_di'})
        return self.prices['plus_di']


    def get_adx_minus(self):
        minus_dm = self.low.diff()
        minus_dm[minus_dm > 0] = 0
        minus_di = abs(
            100 * (minus_dm.ewm(alpha=1 / self.lookback).mean() / self.atr))
        return minus_di

    def update_adx_minus(self):
        tr1 = pd.DataFrame(self.prices['high'] - self.prices['low'])
        tr2 = pd.DataFrame(abs(self.prices['high'] - self.prices['close'].shift(1)))
        tr3 = pd.DataFrame(abs(self.prices['low'] - self.prices['close'].shift(1)))
        frames = [tr1, tr2, tr3]
        tr = pd.concat(frames, axis=1, join='inner').max(axis=1)
        atr = tr.rolling(self.lookback).mean()
        minus_dm = self.prices['low'].diff()
        minus_dm[minus_dm > 0] = 0
        minus_di = abs(
            100 * (minus_dm.ewm(alpha=1 / self.lookback).mean() / atr))
        return minus_di


    def get_minus_di(self):
        self.prices['minus_di'] = pd.DataFrame(self.get_adx_minus()).rename(columns={0: 'minus_di'})
        return self.prices['minus_di']

    def get_adx_smooth(self):
        plus_di = self.get_adx_plus()
        minus_di = self.get_adx_minus()
        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = ((dx.shift(1) * (self.lookback - 1)) + dx) / self.lookback
        adx_smooth = adx.ewm(alpha=1 / self.lookback).mean()
        return adx_smooth

    def update_adx_smooth(self):
        plus_di = self.update_adx_plus()
        minus_di = self.update_adx_minus()
        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = ((dx.shift(1) * (self.lookback - 1)) + dx) / self.lookback
        adx_smooth = adx.ewm(alpha=1 / self.lookback).mean()
        return adx_smooth

    def get_smooth_di(self):
        self.prices['adx'] = pd.DataFrame(self.get_adx_smooth()).rename(columns={0: 'adx'})
        return self.prices['adx']


def stop_buy(prices, n):
    min_price = min(prices)
    min_price = min_price*(1-n/100)
    return min_price


def stop_sell(prices, n):
    max_price = max(prices)
    max_price = max_price*(1+n/100)
    return max_price


def risk_reward_ratio(_target, _stop):
    rr = (_target/_stop)
    return rr


def target(price, n):
    t = price*(1+n/100)
    return t

#
# obj_prices = ADX(prices=prices, lookback=14)
# plus = obj_prices.get_plus_di()
# minus = obj_prices.get_minus_di()
# adx = obj_prices.get_smooth_di()
#
# print('minus\n', minus)
#
# print('-------------update1 ----------------')
# obj_prices.update_price(open=22310, high=19963, low=20135, close=25000, values=23555)
# plus_new = obj_prices.update_adx_plus()
# minus_new = obj_prices.update_adx_minus()
# adx_new = obj_prices.update_adx_smooth()
#
# print('minus\n', minus_new)
#
#
# print('-------------update2 ----------------')
# obj_prices.update_price(open=33333, high=25525, low=36363, close=14145, values=23555)
# plus_new1 = obj_prices.update_adx_plus()
# minus_new1 = obj_prices.update_adx_minus()
#
# adx_new1 = obj_prices.update_adx_smooth()
#
# print('minus\n', minus_new1)
#
# print('-------------update2 ----------------')
# obj_prices.update_price(open=33333, high=25525, low=36363, close=14145, values=23555)
# plus_new2 = obj_prices.update_adx_plus()
# minus_new2 = obj_prices.update_adx_minus()
#
# adx_new2 = obj_prices.update_adx_smooth()
#
# print('minus\n', minus_new2)


# =======================================================================================================


# plt.plot(plus_new, color='#26a69a', label='+ DI 14', linewidth=1.5, alpha=0.3)
# plt.plot(minus_new, color='#f44336', label='- DI 14', linewidth=1.5, alpha=0.3)
# plt.plot(adx_new, color='#2196f3', label='ADX 14', linewidth=3)
# plt.axhline(10, color='grey', linewidth=2, linestyle='--')
# plt.legend()
# plt.show()