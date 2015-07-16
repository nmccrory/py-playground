class underscore(object):
	def reduce(self,list, callback):
		newSum = 0
		for x in list:
			newSum = callback(newSum, x)
		print newSum
	def find(self, list, value):
   		for x in list:
   			if(x == value):
   				print "Found:",x  

	def filter(self, list, callback):
		new_list = []
		for x in list:
			new_list.append(x) if callback(x)==True else False
		print new_list
   		
  	def reject(self, list, callback):
  		rejects = []
  		for x in list:
  			rejects.append(x) if callback(x)==False else True
  		print rejects

_ = underscore()
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
reduces = _.reduce([1,2,3,4,5,6], lambda curr,x: curr+x )
finds = _.find([1,2,3,4,5,6,7], 5)
rejection = _.reject([1,2,3,4,5,6,7], lambda x: x%2 == 0)