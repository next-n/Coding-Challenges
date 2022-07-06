ln = [[1, 2, 3, 4, 5], [2, 4, 5], [6, 8, 1], [1, 8, 6]]
newlist = [a for a in ln if 2 in a]
print(newlist)

h_letter = [letter for letter in "human"]
print(h_letter)

ans = ['even ' + str(i) if i % 2 == 0 else 'odd ' + str(i) for i in range(5)]
print(ans)


def double(x):
	return x * 2


oj = [double(x) for x in range(5)]
print(oj)


def fibonacci(num):
	a, b = 0, 1
	while a < num:
		yield a
		a, b = b, a + b


fftest = fibonacci(10)

pans = [f for f in fftest]
print(pans)
