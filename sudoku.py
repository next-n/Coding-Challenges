def issafe(x, y, num):
	global arr
	# print('num', num, 'index', index)
	# print(arr)
	# print('num', num)
	for i in range(0, 9):
		if arr[x][i] == num:
			return False
	for i in range(0, 9):
		if arr[i][y] == num:
			# print("j", i, y, num)
			return False
	xx = (x // 3) * 3
	yy = (y // 3) * 3
	for ii in range(3):
		for jj in range(3):
			if arr[xx + ii][yy + jj] == num:
				return False

	return True


def sudoku():
	# print(arr)
	global arr
	for x in range(9):
		for y in range(9):
			if arr[x][y] == 0:
				for i in range(1, 10):
					if issafe(x, y, i):
						arr[x][y] = i
						if sudoku():
							return True
						arr[x][y] = 0
				return
	# print(arr)
	return True


global arr
arr = [
	[0, 9, 0, 0, 8, 0, 3, 2, 0],
	[0, 0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 3, 2, 0, 5, 9, 0, 0],
	[0, 2, 4, 0, 0, 7, 0, 0, 0],
	[0, 0, 9, 4, 3, 0, 7, 0, 0],
	[0, 3, 8, 1, 0, 6, 5, 9, 4],
	[0, 1, 2, 7, 4, 9, 0, 8, 5],
	[4, 8, 5, 0, 0, 1, 2, 7, 9],
	[9, 0, 0, 8, 5, 2, 1, 0, 0],
]
sudoku()


# print(arr)


def printlikesodoku():
	sudoku()
	for x in range(9):
		print(str(arr[x]))


printlikesodoku()
