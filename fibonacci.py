def fibonacci(maxx):
	a, b = 0, 1
	while a < maxx:
		yield a
		a, b = b, a + b


ff = fibonacci(10)
# an = [f for f in ff]
# print("an", an)
ax = []
while True:
	try:
		# print('no?')
		ax.append(next(ff))
	except StopIteration:
		print('done')
		print(str(ax))
		break



