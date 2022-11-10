import pandas as pd
import numpy as np
import requests
import matplotlib.pyplot as plt
from math import floor
from termcolor import colored as cl

plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = (20, 10)


# def get_historical_data(symbol, start_date):
#     api_key = '6e7f295a24ae49aa8cb0616edd4e41af'
#     api_url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1day&outputsize=5000&apikey={api_key}'
#     raw_df = requests.get(api_url).json()
#     df = pd.DataFrame(raw_df['values']).iloc[::-1].set_index('datetime').astype(float)
#     df = df[df.index >= start_date]
#     df.index = pd.to_datetime(df.index)
#     return df
# aapl = get_historical_data('AAPL', '2022-05-01')
# print(aapl)

aapl = pd.DataFrame(np.random.randint(low=19503, high=26152, size=(100, 5)), columns=['open', 'high', 'low', 'close', 'values'])
print(aapl)

def get_adx(high, low, close, lookback):
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm[plus_dm < 0] = 0
    minus_dm[minus_dm > 0] = 0
    tr1 = pd.DataFrame(high - low)
    tr2 = pd.DataFrame(abs(high - close.shift(1)))
    tr3 = pd.DataFrame(abs(low - close.shift(1)))
    frames = [tr1, tr2, tr3]
    tr = pd.concat(frames, axis=1, join='inner').max(axis=1)
    atr = tr.rolling(lookback).mean()

    plus_di = 100 * (plus_dm.ewm(alpha=1 / lookback).mean() / atr)
    minus_di = abs(100 * (minus_dm.ewm(alpha=1 / lookback).mean() / atr))
    dx = (abs(plus_di - minus_di) / abs(plus_di + minus_di)) * 100
    adx = ((dx.shift(1) * (lookback - 1)) + dx) / lookback
    adx_smooth = adx.ewm(alpha=1 / lookback).mean()
    return plus_di, minus_di, adx_smooth


aapl['plus_di'] = pd.DataFrame(get_adx(aapl['high'], aapl['low'], aapl['close'], 14)[0]).rename(columns={0: 'plus_di'})
aapl['minus_di'] = pd.DataFrame(get_adx(aapl['high'], aapl['low'], aapl['close'], 14)[1]).rename(
    columns={0: 'minus_di'})
aapl['adx'] = pd.DataFrame(get_adx(aapl['high'], aapl['low'], aapl['close'], 14)[2]).rename(columns={0: 'adx'})
aapl = aapl.dropna()
aapl.tail()
print(aapl)

ax1 = plt.subplot2grid((11, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((11, 1), (6, 0), rowspan=5, colspan=1)
ax1.plot(aapl['close'], linewidth=2, color='#ff9800')
ax1.set_title('AAPL CLOSING PRICE')
ax2.plot(aapl['plus_di'], color='#26a69a', label='+ DI 14', linewidth=3, alpha=0.3)
ax2.plot(aapl['minus_di'], color='#f44336', label='- DI 14', linewidth=3, alpha=0.3)
# ax2.plot(aapl['adx'], color='#2196f3', label='ADX 14', linewidth=3)
ax2.axhline(25, color='grey', linewidth=2, linestyle='--')
ax2.legend()
ax2.set_title('AAPL ADX 14')
plt.show()
print('-----------plus_di---------')
print(aapl['plus_di'])
