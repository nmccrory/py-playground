class Animal(object) :
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		self.health-=1
		return self

	def run(self):
		self.health-=5
		return self

	def displayHealth(self):
		print "Animal Name:", self.name
		print "Health:",self.health
		return self

# animal1 = Animal('Sparky')
# animal1.walk().run().walk().displayHealth()
# class Dog(Animal):
	
# 	def __init__(self, name):
# 		super(Dog, self).__init__(name)
# 		self.health = 150

# 	def pet(self):
# 		self.health += 5
# 		return self

# dog1 = Dog('Michael Jackson')
# dog1.walk().walk().walk().run().run().run().pet().displayHealth()