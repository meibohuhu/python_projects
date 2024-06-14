# Inheritance Example Using Super()
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")

class Dog(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Dog")
        self.breed = breed
        self.toy = toy
    def run(self):
        print(f"{self.name} running!")



blue = Cat("Blue","Scottish Fold", "String")
blue.play()
blue.make_sound("I'm catting!!")

yello = Dog("Yello", "American", "Ball")
yello.run()