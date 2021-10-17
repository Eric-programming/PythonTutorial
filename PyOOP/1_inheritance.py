# Inheritance: Inherit and/or extends from the parent class

# Parent Class
class Car:
    def __init__(self, name="default", price=10):
        self.name = name
        self.price = price

    def drive():
        print("drive...")

    def stop():
        print("stop...")


# Child Class
class RaceCar(Car):
    def __init__(self, name="default race car", price=100):
        super().__init__(name=name, price=price)

    # Extends the functionality
    def super_speed():
        print("super speed...")


car = Car()
car.drive()
car.stop()

race_car = RaceCar()
race_car.drive()
race_car.super_speed()
race_car.stop()
