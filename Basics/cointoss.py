#)simulate coin toss x amount of times
import random 

head_count = 0
tail_count = 0
toss_count = 0

while(toss_count < 30):
	toss = random.randrange(0,100)
	if toss < 50:
		head_count += 1
		result = 'Heads'
	else:
		tail_count += 1
		result = 'Tails'
	print "Throwing a coin...It's", result, "- Got",head_count,"head(s) and",tail_count,"tail(s) so far"
	toss_count += 1
print 'Ending the program'