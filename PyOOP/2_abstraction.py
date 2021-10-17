# Abstract classes allow us to create methods that must be created within any child class

from abc import ABC, abstractmethod  # Abstract Base classes(ABC)
from typing import List


class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("eat")

    @abstractmethod
    def sleep(self):
        print("sleep")


class Bird(Animal):
    def eat(self):
        print("Bird is eating")

    def sleep(self):
        print("Bird is sleeping")


class Pig(Animal):
    def eat(self):
        print("Pig is eating")

    def sleep(self):
        print("Pig is sleeping")


animals: List[Animal] = [Bird(), Pig()]
for animal in animals:
    animal.eat()
    animal.sleep()
