
class Vehicle:
    pass

# instantiate a new Vehicle and save it to a variable called car:
car = Vehicle()

# instantiate a new Vehicle and save it to a variable called boat:
boat = Vehicle()

class User:
	def __init__(self, first, last, age):   ## self refers to current class instance, assign attributes to self
		self.first = first
		self.last = last
		self.age = age
person_2 = User("wendy", "hu", 24)


