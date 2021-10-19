# Abstract class allows us to create methods that must be created within any child class

from abc import ABC, abstractmethod  # Abstract Base classes(ABC)
from typing import List


# You can't initiate an abstract class
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def shout(self):
        print("Shouting...")


# Child class must initiate abstract method
class Bird(Animal):
    def eat(self):
        print("Bird is eating")

    def sleep(self):
        print("Bird is sleeping")


# Child class must initiate abstract method
class Pig(Animal):
    def eat(self):
        print("Pig is eating")

    def sleep(self):
        print("Pig is sleeping")


my_bird = Bird()
my_pig = Pig()

animals: List[Animal] = [my_bird, my_pig]
for animal in animals:
    animal.eat()
    animal.sleep()
    animal.shout()
    print("done")
