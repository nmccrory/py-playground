#)ask user for a test grade 10 times
i = 1
print 'Scores and Grades'
while(i<10):
	grade = input('Please enter a test score between 60 and 100: ')
	if grade < 70:
		print 'Your grade is D'
	elif grade >= 70 and grade <80:
		print 'Your grade is C'
	elif grade >= 80 and grade < 90:
		print 'Your grade is B'
	else:
		print 'Your grade is A'
	i+=1
print 'End of the program. Bye!'