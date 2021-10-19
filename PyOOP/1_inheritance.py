# Inheritance: Inherit and/or extends from the parent class

# Parent Class
class Car:
    def __init__(self, name="default", price=10):
        self.name = name
        self.price = price

    def drive(self):
        print("drive...")

    def stop(self):
        print("stop...")

# Child Class


class RaceCar(Car):
    def __init__(self, name="default race car", price=100, super_speed_value=100):
        super().__init__(name=name, price=price)
        self.super_speed_value = super_speed_value

    # Extends the functionality
    def super_speed(self):
        print(f"super speed at {self.super_speed_value} miles per hour...")


car = Car()
car.drive()
car.stop()

race_car = RaceCar()
race_car.drive()
race_car.super_speed()
race_car.stop()
