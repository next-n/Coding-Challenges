def logging(func):
	def pl(*args):

		return func(*args)

	return pl


def add(x, y):
	return x + y


add_log = logging(add)

print(add_log(1, 2))


