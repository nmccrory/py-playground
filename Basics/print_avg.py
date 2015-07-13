#) print the average of the values in the list
a = [1,2,5,10,255,3]
sum = 0

for n in a:
	sum+=n

avg = sum/len(a)
print avg