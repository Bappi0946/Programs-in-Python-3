a = int(input('Enter first number'))
b = int(input('Enter second number'))
c = int(input('Enter third number'))

if a > b :
	if a > c :
		print(a,'is bigger than',b,'and',c)
	else :
		print(c,'is greater than',a,'and',b)
elif b > c:
	print(b,'is greater than',a,'and',c)
else :
	print(c,'is greater than',a,'and',b)
	
	