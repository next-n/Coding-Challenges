def magicsquare(n):
	ms = [[0 for x in range(n)] for i in range(n)]

	i = n // 2
	j = n - 1
	num = 1
	while num <= n * n:
		# print('num', num)
		if i == -1 and j == n:
			i = 0
			j = n - 2
		else:
			u = 0
		# if i >= n:
		# 	# print(i)
		# 	temp = (i // (n - 1))
		# 	i = temp - (temp * 1)
		# if i < 0:
		# 	temp = (abs(i) // 3) + 1
		# 	i = (temp * n) + i
		# if j >= n:
		# 	temp = (j // (n - 1))
		# 	j = temp - (temp * 1)
		# if j < 0:
		# 	temp = (abs(j) // n) + 1
		# 	j = (temp * 3) + j
		if j == n:
			j = 0
		if i < 0:
			i = n - 1
		# print(i, j)
		if ms[i][j] != 0:

			i += 1
			j -= 2
			continue
		else:
			ms[i][j] = num
			num += 1
		i -= 1
		j += 1
	print(ms)


magicsquare(3)

# if ms[i][j] == 0:
# 	print("zero", i, j)
# 	ms[i][j] = x
# 	i -= 1
# 	j += 1
# 	if i == -1 and j == n:
# 		i = 0
# 		j = n - 2
# 	if i < 0 and j != n:
# 		i = 2
# 	if j > 2 and i != -1:
# 		j = 0
# elif ms[i][j] != 0:
# 	print('not zero before', i, j)
# 	i += 1
# 	j -= 2
# 	if i == -1 and j == n:
# 		i = 0
# 		j = n - 2
# 	elif i > 2:
# 		temp = (i // 2)
# 		i = temp - (temp * 1)
# 	if j < 0 and i != -1:
# 		temp = (abs(j) // 3) + 1
# 		j = (temp * 3) + j
# 	print('not zero after', i, j)
# 	ms[i][j] = x
# 	i -= 1
# 	j += 1
# 	if i == -1 and j == n:
# 		i = 0
# 		j = n - 2
# 	if i < 0 and j != n:
# 		i = 2
# 	if j > 2 and i != -1:
# 		j = 0
