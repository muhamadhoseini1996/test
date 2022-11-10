from numpy import random, mean


class ADX:
    prices = list(random.randint(low=1, high=10, size=5))
    average_history = [0, 0, 0, 0, 0]

    def moving_average(self, price):
        print('prices', ADX.prices)
        ADX.prices.pop(0)
        ADX.prices.append(price)
        print('prices', ADX.prices)
        avg = mean(ADX.prices)
        if len(ADX.average_history) >= 5:
            ADX.average_history.pop(0)
        ADX.average_history.append(avg)
        print('average = ', avg)
        print('average history', ADX.average_history)
        return avg


live_adx = ADX()
live_adx.moving_average(1)
live_adx.moving_average(2)
live_adx.moving_average(3)
live_adx.moving_average(4)
live_adx.moving_average(5)
live_adx.moving_average(6)
