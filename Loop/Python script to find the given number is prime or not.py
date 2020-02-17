p = int(input('Enter a number :'))

for a in range(2,p) :
	if p % a == 0 :
		print(p,'is not a prime number')
		break  
else :
		print(p,'is a prime number ')
		