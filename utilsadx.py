from .refactoradx import *
import pandas as pd


data = pd.DataFrame(np.random.randint(low=19503, high=26152, size=(100, 5)), columns=['open', 'high', 'low', 'close', 'values'])

test_plus = ADX(data, data['high'], data['low'], data['close'], 14)
test_minus = ADX(data, data['high'], data['low'], data['close'], 14)
test_adx = ADX(data, data['high'], data['low'], data['close'], 14)
