import numpy as np
import pandas as pd


class ADX:
    """
        #TODO: write docstring for this data type
    """
    def __init__(self, prices, windows_size, high, low, close, lookback):
        self.prices = prices
        self.high = high
        self.low = low
        self.close = close
        self.lookback = lookback
        self.tr1 = pd.DataFrame(self.high - self.low)
        self.tr2 = pd.DataFrame(abs(self.high - self.close.shift(1)))
        self.tr3 = pd.DataFrame(abs(self.low - self.close.shift(1)))
        self.frames = [self.tr1, self.tr2, self.tr3]
        self.tr = pd.concat(self.frames, axis=1, join='inner').max(axis=1)
        self.update_plus = list(self.tr[-windows_size:])
        self.atr = self.tr.rolling(self.lookback).mean()

    def get_adx_plus(self):
        plus_dm = self.high.diff()
        plus_dm[plus_dm < 0] = 0
        plus_di = 100 * (plus_dm.ewm(alpha=1 / self.lookback).mean() / self.atr)
        return plus_di

    def update_adx_plus(self, new_price):
        self.update_plus.pop(0)
        self.update_plus.append(new_price)
        result = np.mean(self.update_plus)
        return result

    def get_adx_minus(self):
        minus_dm = self.low.diff()
        minus_dm[minus_dm > 0] = 0
        minus_di = abs(100 * (minus_dm.ewm(alpha=1 / self.lookback).mean() / self.atr))
        return minus_di

    def get_adx_smooth(self):
        plus_di = self.get_adx_plus()
        minus_di = self.get_adx_minus()
        dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
        adx = ((dx.shift(1) * (self.lookback - 1)) + dx) / self.lookback
        adx_smooth = adx.ewm(alpha=1 / self.lookback).mean()
        return adx_smooth


data_prices = pd.DataFrame(np.random.randint(low=19503, high=26152, size=(100, 5)), columns=['open', 'high', 'low', 'close', 'values'])
test_plus = ADX(data_prices, 5, data_prices['high'], data_prices['low'], data_prices['close'], 14)
test_minus = ADX(data_prices, 5, data_prices['high'], data_prices['low'], data_prices['close'], 14)
test_adx = ADX(data_prices, 5, data_prices['high'], data_prices['low'], data_prices['close'], 14)

data_prices['plus_di'] = pd.DataFrame(test_plus.get_adx_plus()).rename(columns={0: 'plus_di'})
data_prices['minus_di'] = pd.DataFrame(test_minus.get_adx_minus()).rename(columns={0: 'minus_di'})
data_prices['adx'] = pd.DataFrame(test_adx.get_adx_smooth()).rename(columns={0: 'adx'})

data_prices = data_prices.dropna()
data_prices.tail()

print('-----------plus_di---------')
print(data_prices['plus_di'])
#
print('-----------get_adx_minus---------')
print(data_prices['minus_di'])

print('-----------get_adx_smooth---------')
print(data_prices['adx'])

