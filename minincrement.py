def findsum(n):
	sumtotal = 0
	while n != 0:
		digit = n % 10
		sumtotal += digit
		n //= 10
	return sumtotal


def howmanydigit(n):
	digitcount = 0
	while n != 0:

		digitcount += 1
		n //= 10
	return digitcount


def minincrement(n, s):
	checksum = findsum(n)
	print(checksum)
	if checksum <= s:
		return 0
	digitcount = howmanydigit(n)
	p = 1
	ans = 0
	for x in range(digitcount):

		digit = (n // p) % 10
		# print(digit)
		if digit != 0:

			adddigit = p * (10 - digit)

			n += adddigit
			ans += adddigit

			checksum -= (digit - 1)
		if findsum(n) <= s:
			break

		p *= 10
	return ans


ne = 345899211156769
sa = 20
# minincrement(ne, sa)
# print(345899211156769)
print(minincrement(ne, sa))
# print(345899211156769 + 100788843231)

