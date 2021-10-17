# Basic class
class Person:
    pass


# Instance of a Person class
person1 = Person()
person2 = Person()
is_same_type = type(person1) == type(person2)


# Point Class
class Point:
    def __init__(self, x=0, y=0, **kwargs) -> None:
        self.x = x
        self.y = y
        # You can do this to update the self.__dict__
        self.__dict__.update(kwargs)

        # but you can't do the following:
        # for key, value in kwargs.items():
        # self[key] = value

    def get_location(self):
        return (self.x, self.y)


p1 = Point(x=1, y=1)
p1_location = p1.get_location()
p2 = Point()
p2_location = p2.get_location()
p3 = Point(t=1)
p3_location = p3.get_location()


# Class with Static methods/variables
class Location:
    x = 1
    y = None

    @staticmethod
    def get_location():
        return (Location.x, Location.y)


print(p3)
