import math


def finddis(a, b, c, d):
	ans = (math.sqrt((c - a) ** 2 + (d - b) ** 2))
	return ans


print(finddis(3, 4, 4, 3))
