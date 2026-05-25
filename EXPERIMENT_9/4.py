# 4 . Create a class to implement method Overriding.
class Animal:
    def sound(self):
        print("Animals make different sounds")

class Dog(Animal):
    def sound(self):
        print("The dog barks")

class Cat(Animal):
    def sound(self):
        print("The cat meows")

animal = Animal()
dog = Dog()
cat = Cat()

animal.sound()
dog.sound()
cat.sound()
