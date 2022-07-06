def minimumDistances(a):
	result = []
	for x in range(len(a) - 1):
		y = x + 1
		for y in range(y, len(a)):
			# print(a[x], a[y])
			if a[x] == a[y]:
				ac = y - x
				result.append(ac)
	return min(result)


print(minimumDistances([7, 1, 3, 4, 1, 7]))

