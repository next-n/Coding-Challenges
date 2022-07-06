def solveone(ar, digit, temp, ans):
	# print('we are calling solveone', ans)
	# print('digit', digit)

	if digit == len(ar):
		if temp != [0, 0, 0]:
			# print('a')
			printsolve(ar, temp, ans)
			return digit
		else:
			# print('b')
			# print(ans)
			return ans
	temp[digit] = 1
	solveone(ar, digit + 1, temp, ans)
	temp[digit] = 0
	solveone(ar, digit + 1, temp, ans)
	# print('c')
	return ans


def printsolve(ar, temp, ans):
	answ = []
	for x in range(len(temp)):
		if temp[x] == 1:
			answ.append(ar[x])
	# print('answ', answ, 'temp', temp)
	ans.append(answ)


aki = []
pans = solveone([1, 2, 3], 0, [-1, -1, -1], aki)

print(pans)


def solvetwo(ar):
	ans = []
	for mask in range(1, 1 << len(ar)):
		cur = []
		for x in range(len(ar)):
			if mask & 1 << x != 0:
				cur.append(ar[x])

		ans.append(cur)
	print(ans)


solvetwo([1, 2, 3])
