#)defining multiply function
def multiply(list, multiple):
	x = []
	for n in list:
		x.append(n*multiple)
	print x


a = [2, 4, 10, 16]

#)example pluggin in the number 2 and 'a' list
multiply(a, 2)