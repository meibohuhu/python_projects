
## the ability to define a class which inherits from another class(a "base" or "paraent")


## properties: respect conventions, reduce duplicates
## class variables, class methods

class Animal:
    cool = True   ## class variable
    def make_sound(self, sound):
        print(f"Make this sound {sound}")

class Cat(Animal):
    pass

gandalf = Cat()
print(gandalf.cool)
