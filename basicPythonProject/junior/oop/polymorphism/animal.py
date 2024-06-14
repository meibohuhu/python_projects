## override

class Animal():
    def speak(self):
        raise NotImplementedError("Subclass needs to be implemented")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meeow")

dog = Dog()
dog.speak()
cat = Cat()
cat.speak()
