def mergesort(arr):
	if len(arr) == 1:
		return arr
	start = 0
	end = len(arr)
	mid = (end - start) // 2
	if end - 1 > start:
		a = mergesort(arr[start:mid])
		b = mergesort(arr[mid:end])
		return merge(a, b)


def merge(a, b):
	i = 0
	j = 0
	result = []
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			result.append(a[i])
			i += 1
		else:
			result.append(b[j])
			j += 1
	while i < len(a):
		result.append(a[i])
		i += 1
	while j < len(b):
		result.append(b[j])
		j += 1
	return result


print(mergesort([4, 5, 7, 12, 2]))
