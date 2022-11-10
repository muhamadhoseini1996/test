import pandas as pd
import numpy as np


class SimpleMovingAvrage:
    """
        #TODO: write docstring for this data type
    """

    def __init__(self, prices, windows_size):
        self.prices = self.__pandas_series(prices)
        self.update_avrage_frame = list(prices[-windows_size:])
        self.windows_size = windows_size
        self.avrages = self.moving_avrage(prices,
                                          windows_size)
        self.avrages.reset_index(drop=True, inplace=True)

    def moving_avrage(self, data_frame, window_size):
        # TODO: check dataFrame is pandas serise
        result = data_frame.rolling(window_size).mean()
        result.dropna(inplace=True)
        return result

    def update_moving_avrage(self, new_price):
        self.update_avrage_frame.pop(0)
        self.update_avrage_frame.append(new_price)
        result = np.mean(self.update_avrage_frame)
        self.__append_avrage(result)
        return result

    def get_avrage(self, index=None):
        avrages = list(self.avrages)
        if index == None:
            return avrages
        elif index < len(index):
            return avrages[index]
        return None

    def get_last_avrage(self):
        return self.get_avrage(index=-1)

    def __append_avrage(self, new_avrage):
        # TODO: check size of self.avrage and append new value
        self.avrages[len(self.avrages)] = new_avrage

    def __pandas_series(self, prices):
        # TODO check input this pandas serize
        return prices

    def __getitem__(self, index):
        try:
            return self.get_avrage(index)
        except IndexError:
            return None

    def __str__(self):
        return str(self.get_avrage())


# def cumulative_moving_average(self, data_frame, window_size):
#     # TODO: check dataFrame is pandas serise
#     result = data_frame.expanding(window_size).mean()
#     result.dropna(inplace=True)
#     return result


# def exponential_moving_average(self, data_frame, window_size):
#     # TODO: check dataFrame is pandas serise
#     result = data_frame.ewm(span=window_size).mean()
#     result.dropna(inplace=True)
#     return result


# def update_moving_avrage(self, last_mean, new_price, size):
#     result = last_mean + (new_price - last_mean)/size
#     return result

