#) creating a bikes class

class Bike():
	def __init__(self, max_speed, price, miles):
		self.max_speed = max_speed
		self.price = price
		self.miles = miles

	def displayinfo(self):
		print "Price:",self.price
		print "Speed:",self.max_speed
		print "Miles:", self.miles
		return self

	def drive(self):
		self.miles += 10
		print 'Driving...'
		return self

	def reverse(self):
		self.miles -= 5
		print 'Reversing...'
		return self

bike1 = Bike(140, 20000, 60000)

bike1.drive().drive().reverse().displayinfo()