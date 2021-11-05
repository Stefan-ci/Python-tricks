
for row in range(10):
	for col in range(10):
		if row + col == 9 or row - col == 0:
			print('#', end=' ')
		else:
			print(end=' ')
	print()
