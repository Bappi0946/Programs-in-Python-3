n = int(input('Enter a number'))

for q in range(2,n+1):
	for a in range(2,q):
		if q % a == 0:
			break
	else:
		print(q)