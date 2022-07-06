def checkminustwo(vec, n):
	ans = 0
	for mask in range(1 << n):
		cur = 0
		for i in range(n):
			if mask & (1 << i) != 0:
				cur += vec[i]
		if cur == sum(vec) - 2:
			ans += 1
	return ans


pn = checkminustwo([2, 0, 2, 3, 1], 5)
print(pn)
