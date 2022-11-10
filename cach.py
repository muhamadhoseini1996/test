





# def update_adx(price, param):
#     old_prices = price.truncate(before=1).reset_index()
#     new_price = old_prices.append({"open": param.get('open'),
#                                    "high": param.get('high'),
#                                    "low": param.get('low'),
#                                    "close": param.get('close'),
#                                    "values": param.get('values')},
#                                   ignore_index=True)
#     obj_prices = ADX(new_price['high'], new_price['low'], new_price['close'], 14)
#     return obj_prices, new_price


# print('type', type(prices))
# print('----------------------------')
# params = dict(open=19000, high=21000, low=19520, close=23112, values=19234)
# obj = update_adx(prices, params)
# plus = plus_di(obj[1], obj[0].get_adx_plus())
# plus = plus.dropna()
# plus.tail()
# # print('obj\n', plus)


# print('----------------------------')
# params1 = dict(open=19988, high=20300, low=24200, close=23221, values=19366)
# obj1 = update_adx(obj[1], params1)
# plus1 = plus_di(obj1[1], obj1[0].get_adx_plus())
# plus1 = plus1.dropna()
# plus1.tail()
# print('obj1\n', plus1)
























#
# plt.plot(plus, color='#26a69a', label='+ DI 14', linewidth=1.5, alpha=0.3)
# plt.plot(minus, color='#f44336', label='- DI 14', linewidth=1.5, alpha=0.3)
# plt.plot(adx, color='#2196f3', label='ADX 14', linewidth=3)
# plt.axhline(10, color='grey', linewidth=2, linestyle='--')
# plt.legend()
# plt.show()

