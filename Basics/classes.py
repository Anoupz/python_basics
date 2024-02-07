# How class are defined and used in Python


# Create a class
class Person:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")


# Create an object of the class
p = Person("Max", 28)
p.say_hello()
# Hello, my name is Max and I am 28 years old
