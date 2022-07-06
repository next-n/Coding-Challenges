def rightrotatedarray(ar, k):
	minus = len(ar) - k
	first = ar[minus: len(ar)]
	sec = ar[0:minus]
	newary = ""
	for x in range(len(first)):
		newary += str(first[x]) + " "
	for x in range(len(sec)):
		newary += str(sec[x]) + " "
	return newary


ar = [1, 2, 3, 4, 5]
k = 4
print(rightrotatedarray(ar, k))
