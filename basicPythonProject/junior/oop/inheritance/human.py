
## properties for getter and setter

class Human:
    def __init__(self, first, last, age):
        print("jhh")
        self.first = first
        self.last = last
        self._age = max(age, 0)      ## _age only for internal usage

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = max(age, 0)

    @property
    def fullName(self):
        return f"{self.first} {self.last}"

    @fullName.setter
    def fullName(self, name):
        self.first, self.last = name.split(" ")


jane = Human("hu", "wendy", 19)
jane.age = 29
print(jane.age)

jane.fullName = "Phonenix Jin"     ## setting
print(jane.first)

