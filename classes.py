class Animal:
    def __init__(self,name):
        self.name = name
        print("Animal created")
    def eat(self):
        print("Eating")
    def breathe(self):
        print("Breathing")

class Dog(Animal):
    def bark(self):
        print("Barking")
class Cat(Animal):
    def meow(self):
        print("meow")

cat1 = Cat("Chukuw")
cat1.eat()
cat1.meow()
print(cat1.name)