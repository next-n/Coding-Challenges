def test():
	ar = [[1, 3, 3], [4, 2, 5], [1, 2, 5]]
	ar.sort(key=lambda a: (a[0], a[1]))
	te = [1, 2, 3]
	numb = te.pop(0)
	print(numb)
	print(ar)


# test()


def maxoverlap(ar):
	# print(ar)
	ar.sort(key=lambda a: (a[0], a[1]))
	pqueue = []
	maxx = 0
	ans = 0
	# print(ar)
	for x in range(len(ar)):
		# print('for')
		while len(pqueue) != 0:
			# print(pqueue)
			if pqueue[0][0] >= ar[x][0]:
				# print("break", ar[x])
				print(pqueue)
				break

			pq = pqueue.pop(0)
			# print("pq", pq)
			maxx = max(maxx, pq[1])

		ans = max(ans, maxx + ar[x][2])
		pqueue.append([ar[x][1], ar[x][2]])
		pqueue.sort(key=lambda a: a[0])
	print('ans', ans)
	return ans


testarray = [[1, 4, 2], [3, 8, 4], [4, 7, 6], [8, 10, 5]]
maxoverlap(testarray)
