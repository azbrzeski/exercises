from random import randint
from max_sum_sublist import performance_check

# You are a professional robber planning to rob
# houses along a street. Each house has a certain
# amount of money stashed, the only constraint
# stopping you from robbing each of them is that
# adjacent houses have security systems connected,
# and it will automatically contact the police
# if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money
# of each house, return the maximum amount of money you can
# rob tonight without alerting the police.
#
# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
# Constraints:
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400


list1 = [1, 2, 3, 1]
list2 = [2, 7, 9, 3, 1]
list3 = [0, 1, 9, 0, 2, 3, 1, 1, 4, 2, 1, 5, 5, 7, 5, 1, 9, 12, 1, 4, 2, 2, 6, 4, 4, 0]
list4 = []
list5 = [1, 6, 8, 2, 3, 8, 3, 5, 8, 9, 5, 2, 2, 4, 1, 5, 8, 3, 4, 8, 9, 4, 6, 4, 7, 5, 1, 20, 6, 8, 11]
list6 = [1, 2, 1, 12, 16, 90]
list7 = [5, 2, 1, 40, 15]

test_list = [list1, list2, list3, list4, list5, list6, list7]


def max_sum_optimization(input_list, _i=0, cache={-2: (0, []), -1: (0, [])}, *, clear_cache=True):

	if clear_cache:
		cache.clear()
		cache[-2] = (0, [])
		cache[-1] = (0, [])

	# if not input_list:
	# 	return None, None

	if _i >= len(input_list):
		_i = _i - 1
		return cache[_i] if cache[_i][0] > cache[_i - 1][0] else cache[_i - 1]

	if _i not in cache.keys():
		if cache[_i - 1][0] > cache[_i - 2][0] + input_list[_i]:
			cache[_i] = cache[_i - 1]
		else:
			cache[_i] = (cache[_i - 2][0] + input_list[_i], [*cache[_i - 2][1], input_list[_i]])

	return max_sum_optimization(input_list, _i+1, clear_cache=False)


if __name__ == '__main__':

	for test_item in test_list:
		print('--------------------------')
		print(test_item)
		print(f'Not reversed: {max_sum_optimization(test_item)}')
		print(f'Reversed:     {max_sum_optimization(test_item[::-1])}')

	test_list = []

	for i in range(300):
		test_list.append(randint(0, 400))

	result_not_reversed = max_sum_optimization(test_list)
	result_reversed = max_sum_optimization(test_list[::-1])

	print('--------------------------')
	print(test_list)
	print(f'Not reversed: {result_not_reversed}')
	print(f'Reversed:     {result_reversed[0], result_reversed[1][::-1]}')

	performance_check(1000, max_sum_optimization, test_list)
