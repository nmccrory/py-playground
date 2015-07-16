#importing the animal class
from animal import Animal
#definining Dog class
class Dog(Animal):
	#init params must match Animal __init__ params
	def __init__(self, name):
		super(Dog, self).__init__(name) #<----pass name to Animal here
		self.health = 150

	def pet(self):
		self.health += 5
		return self
#defining new instance of Dog
dog1 = Dog('Crypto')
#chaining class methods
dog1.walk().walk().walk().run().run().run().pet().displayHealth()