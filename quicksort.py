def partion(arr, low, high):

	pivot = arr[low]
	i = low
	j = high
	while i < j:
		i += 1
		j -= 1
		while arr[i] <= pivot and i < high - 1:
			i += 1
		while arr[j] > pivot:
			j -= 1
		if i < j:
			arr[i], arr[j] = arr[j], arr[i]
	arr[low], arr[j] = arr[j], arr[low]
	return j


def quicksort(arr, low, high):
	# print(arr, 'low', low, 'high', high)
	if high - 1 > low:
		j = partion(arr, low, high)
		# print('j', j, arr, low, high)
		quicksort(arr, low, j)
		# print('buuffjj', j)
		quicksort(arr, j + 1, high)


adsd = [10, 5, 121, 6, 14]
quicksort(adsd, 0, 5)
print(adsd)





# arrara = [10, 3, 12, 14, 5, 6]
# # uquicksort(arrara)
# #
# # print(arrara)
# # 5, 3, 6
# # print(partition([5, 3, 6]))
#
# uquicksort(arrara, 0, 6)
#
# print(arrara)
