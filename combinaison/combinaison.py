
def combin(n, k):
	if k > n//2:
		k = n - k
	x = 1
	y = 1
	i = n - k + 1
	while i <= n:
		x = (x*i) // y
		y += 1
		i += 1
	return x
print(combin(3, 2))