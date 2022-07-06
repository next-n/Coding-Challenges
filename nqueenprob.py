def leftupper(board, i, j):
	while (i - 1) >= 0 and (j - 1) >= 0:
		if board[i - 1][j - 1] == 1:
			return False
		i -= 1
		j -= 1
	return True


def rightupper(board, i, j):
	while i - 1 >= 0 and j + 1 < len(board):
		if board[i - 1][j + 1] == 1:
			return False
		i -= 1
		j += 1
	return True


def leftdown(board, i, j):
	while i + 1 < len(board) and j - 1 >= 0:
		if board[i + 1][j - 1] == 1:
			return False
		i += 1
		j -= 1
	return True


def rightdown(board, i, j):
	while (i + 1) < len(board) and (j + 1) < len(board):
		if board[i + 1][j + 1] == 1:
			return False
		i += 1
		j += 1
	return True


def issafe(board, i, j, iary, jary):
	one = leftupper(board, i, j)
	two = leftdown(board, i, j)
	three = rightdown(board, i, j)
	four = rightupper(board, i, j)
	if not (i in iary or j in jary):
		if one and two and three and four:
			return True
		else:
			return False
	else:
		return False


def nqueenprob(board, col, iary, jary):
	# this is final answer
	if col >= len(board):
		return True
	# looping i through different column(j)
	for x in range(len(board)):
		# checking issafe column, row and diagonal
		if issafe(board, x, col, iary, jary):
			board[x][col] = 1
			# insert x to iary and col to jary for fast check same column or row
			iary.append(x)
			jary.append(col)
			# recursive function with col plus one
			if nqueenprob(board, col + 1, iary, jary):
				return True
			# this is time for backtrack and move on with row loop(i/x)
			iary.pop(len(iary) - 1)
			jary.pop(len(jary) - 1)
			board[x][col] = 0
	return False


boardi = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
iry = []
jry = []
nqueenprob(boardi, 0, iry, jry)
print(boardi)

# This recursive or backtrack is simple. They start with column zero and loop row from 0 to end minus 1.
# When you find a spot within issafe, you move into new column and start loop of row from zero again
# when you can't find anyspot after looping all row, you need to back to before a column and
#   make that [row][col] back to zero and move to new row(i/x) within row loop

# A simple thing is when you complete looping row(x/i) and still can't find spot! your code backtrack to
#  last column and make that spot back to zero and move on row loop. Same thing happen over and over.



