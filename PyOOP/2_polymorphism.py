# Polymorphism allows us to have many methods with same name but different characteristics
# Python can only use overriding but not overloading.

# Parent Class
class Car:
    def __init__(self, name="default", price=10):
        self.name = name
        self.price = price

    def drive(self, speed):
        print(f"driving at {speed} mile per hour...")

    def stop(self):
        print("stop...")


# Child Class
class RaceCar(Car):
    def __init__(self, name="default race car", price=100):
        super().__init__(name=name, price=price)

    # Extends the functionality
    def super_speed(self,):
        print("super speed...")

    def drive(self):
        print("Racecar driving...")


# overloading allow us to have many methods with same name but different parameter and functionality.
car = Car()
# car.drive()  # this will throw an error
car.drive(100)

# overriding allows us to override the methods of a parent class from its child class.
race_car = RaceCar()
race_car.drive()
