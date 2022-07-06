import re
from functools import partial

in_str = "1, 2, 3, 4"
result = re.findall(r"a", in_str)
print(result)

res = re.split(r",\s", in_str).__iter__()
nex = [int(i) for i in res]
print(nex)

print(re.search(r'a{2,4}i', 'maaain'))


def base(e):
	print("exponent is", e)
	return lambda b: b ** e


cube = base(3)
print(cube(4))


def afha(a, b, c, d):
	print('a is', a)
	print('b is', b)
	print('c is', c)
	print('d is', d)
	return a + b + c + d


g = partial(afha, 1, 2)

h = partial(g, 3)

h(4)


def power(axpo, bxpo, cxpo, dxpo, expo, fxpo, gxpo):
	print(cxpo)
	print(expo)
	return gxpo


firstsquare = partial(power, 1, 2, dxpo=1, fxpo=1)

sec = partial(firstsquare, expo=5)

t = partial(sec, gxpo=7)

print(t(3))


