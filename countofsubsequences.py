n = 5
for mask in range(1 << n):
	cur = 0
	for i in range(n):
		# print("mask is", mask, "i start loop", i)
		# print(mask, 1 << i)
		# print("mask & 1 << i \\", mask & (1 << i))
		if mask & (1 << i) != 0:
			print("here if clause and i is", i)
	print('out')


