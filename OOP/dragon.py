from animal import Animal 

class Dragon(Animal):
	def __init__(self, name):
		self.health = 170
		super(Dragon, self).__init__(name)

	def fly(self):
		self.health -= 10
		return self


dragon1 = Dragon('Fiery')

dragon1.fly().walk().walk().fly().run().fly().displayHealth()