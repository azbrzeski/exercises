from random import randint
from time import perf_counter

# You are given an array prices where prices[i]
# is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing
# a single day to buy one stock and choosing
# a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve
# from this transaction. If you cannot achieve
# any profit, return 0.

# Example 1:
#
# Input: prices = [7 ,1 ,5 ,3 ,6 ,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell
# on day 5 (price = 6), profit = 6- 1 = 5.
# Note that buying on day 2 and selling on day 1
# is not allowed because you must buy before
# you sell.

# Example 2:
#
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: In this case, no transactions are
# done and the max profit = 0.
#
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
prices3 = [7, 75, 6, 72, 5, 70]
prices4 = [7, 75, 6, 72, 5, 1]

test_list = [prices1, prices2, prices3, prices4]


def buy_and_sell(price_list=[], *, max_price=(0, 0, 0), cache_clear=True):

	if cache_clear:
		max_price = (0, 0, 0)

	if len(price_list) <= 1:
		return max_price

	buy_price = min(price_list)
	buy_index = price_list.index(buy_price)

	sell_price = max(*price_list[buy_index::], max_price[2])

	if max_price[0] <= sell_price - buy_price:
		max_price = (sell_price - buy_price, buy_price, sell_price)
	else:
		return max_price

	return buy_and_sell(price_list[:buy_index], max_price=max_price, cache_clear=False)


def performance_check(repeats: int, func, *args, list_size=1000, rand_start=0, rand_end=10000000, **kwargs):

	perf_set = set()
	for i in range(repeats):
		t_list = []
		for k in range(list_size):
			t_list.append(randint(rand_start, rand_end))

		time_start = perf_counter()
		func(t_list, *args, **kwargs)
		time_end = perf_counter()

		perf_set.add(time_end-time_start)

	print('--------------------------------')
	print('Function name: ', func.__name__)
	print('Repeats:       ', repeats)
	print('List size:     ', list_size)
	print('Time:          ', sum(perf_set))
	print('Avg. time:     ', sum(perf_set)/len(perf_set))
	print('Max time:      ', max(perf_set))
	print('Min time:      ', min(perf_set))


if __name__ == '__main__':

	for test_item in test_list:
		print('----------------------------')
		print(test_item)
		print('List search: ', buy_and_sell(test_item))

	test_list = []
	for i in range(100000):
		test_list.append(randint(0, 10000000))

	print('----------------------------')
	print(buy_and_sell(test_list))

	performance_check(10000, buy_and_sell)
