from time import perf_counter
from random import randint

DEBUG = False

# Code comparing performance of two functions doing the same task
# but using different method.
# One of the functions is creating list to store potential result list
# And the other is storing only indices of result
# and creating result list at the return statement
#
# The task is to search through given list and find the sublist
# with maximal possible sum of elements.
# arr1..arr7 are list created for functions testing
# with given results.


arr1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# expected result_sum 6 -> result_list [4, -1, 2, 1]

arr2 = [1]
# expected result_sum 1 -> result_list [1]

arr3 = [5, 4, -1, 7, 8]
# expected result_sum 23 -> result_list [5, 4, -1, 7, 8]

arr4 = [-2, -1, -3, -4]
# expected result_sum -1 -> result_list [-1]

arr5 = [-1, 2, 3]
# expected result_sum 5 -> result_list [2, 3]

arr6 = [1, 2, -1]
# expected result_sum 3 -> result_list [1, 2]

arr7 = []
# expected result_sum None -> result_list []

test_list = [arr1, arr2, arr3, arr4, arr5, arr6, arr7]


def max_sublist_list(array):
	if not array or len(array) <= 1:
		return *array, array

	# Data initiation after checking if list is not None
	sublist_sum = result_sum = array[0]
	sub_components = [array[0]]
	result_sublist = []

	for i in array[1:]:
		if sublist_sum <= 0:
			sublist_sum = i
			sub_components = [i]
		else:
			sublist_sum += i
			sub_components.append(i)

		if sublist_sum > result_sum:
			result_sum = sublist_sum
			result_sublist = [*sub_components]

		# if DEBUG:
		# 	print('	-	-	-	-	-	-	-	-')
		# 	print(f'Iteration: {i}')
		# 	print(f'sublist_sum: {sublist_sum}, result_sum:{result_sum}')
		# 	print(f'sub_components: {sub_components}')
		# 	print(f'result_sublist: {result_sublist}')

	return result_sum, result_sublist


def max_sublist_indices(array):
	if not array or len(array) <= 1:
		return *array, array

	# Data initiation after checking if list is not None
	sublist_sum = result_sum = array[0]
	components_index_start = components_index_end = 0
	result_index_start = result_index_end = 0

	for i in range(1, len(array)):
		if sublist_sum <= 0:
			sublist_sum = array[i]
			components_index_start = i
			components_index_end = i
		else:
			sublist_sum += array[i]
			components_index_end += 1

		if sublist_sum > result_sum:
			result_sum = sublist_sum
			result_index_start = components_index_start
			result_index_end = components_index_end

		# if DEBUG:
		# 	print('-	-	-	-	-	-	-	-	-	-	-')
		# 	print(f'Iteration: {i}')
		# 	print(f'sublist_sum: {sublist_sum}, result_sum: {result_sum}')
		# 	print(f'components_index_start: {components_index_start}, components_index_end: {components_index_end}')
		# 	print(f'result_index_start: {result_index_start}, result_index_end: {result_index_end}')

	return result_sum, [array[i] for i in range(result_index_start, result_index_end+1)]


def performance_check(repeats: int, func, *args, **kwargs) -> None:
	"""
	Function checking performance of execution function "func" repeated "repeats" times.
	function prints the results to stdout.
	"""
	time_start = perf_counter()

	for i in range(repeats-1):
		func(*args, **kwargs)

	# last execution is simply to assign results to variables
	result_sum, result_list = func(*args, **kwargs)

	time_end = perf_counter()

	print('-----------------------------------')
	print(f'Function name: {func.__name__}')
	print(f'Repeats: {repeats}')
	print(f'Test list length: {len(*args)}')
	print(f'Execution time: {time_end - time_start}s')
	print(f'Result sum: {result_sum}')
	print(f'Result list: {result_list}')
	print(f'Result list length: {len(result_list)}')


if __name__ == "__main__":
	for test_item in test_list:
		print('-----------------------------------')
		print(f'Original list: {test_item}')
		print(f'Results usign max_subarraly_list: {max_sublist_list(test_item)}')
		print(f'Results usign max_sublist_indices: {max_sublist_indices(test_item)}')

	test_list = []
	for i in range(1000):
		test_list.append(randint(-5, 10))

	performance_check(5000, max_sublist_list, test_list)
	performance_check(5000, max_sublist_indices, test_list)
