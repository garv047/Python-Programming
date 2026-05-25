# 3.
class Parent:
    def feature1(self):
        print("Feature 1 from Parent")

class Child(Parent):
    def feature2(self):
        print("Feature 2 from Child")

obj = Child()
obj.feature1()
obj.feature2()

# Multiple inheritence
class Father:
    def skill1(self):
        print("Father's skill")

class Mother:
    def skill2(self):
        print("Mother's skill")

class Child(Father, Mother):
    def skill3(self):
        print("Child's own skill")

obj = Child()
obj.skill1()
obj.skill2()
obj.skill3()

#Multilevel inheritence
class Grandparent:
    def property1(self):
        print("Grandparent's property")

class Parent(Grandparent):
    def property2(self):
        print("Parent's property")

class Child(Parent):
    def property3(self):
        print("Child's property")

obj = Child()
obj.property1()
obj.property2()
obj.property3()

# Heirarchical inheritence
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")

d = Dog()
c = Cat()
d.speak()
d.bark()
c.speak()
c.meow()

# Hybrid inheritence
class School:
    def func1(self):
        print("This is the school")

class Student1(School):
    def func2(self):
        print("This is student 1")

class Student2(School):
    def func3(self):
        print("This is student 2")

class SchoolDetails(Student1, Student2):
    def func4(self):
        print("This is the school details class")

obj = SchoolDetails()
obj.func1()
obj.func2()
obj.func3()
obj.func4()
