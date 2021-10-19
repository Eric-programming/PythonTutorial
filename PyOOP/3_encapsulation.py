# Encapsulation allow us to put restrictions on accessing variales/methods
class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current


my_counter = Counter()
my_counter.increment()
print(my_counter.value())
# We can still access and change current outside of Counter
print(my_counter.current)
my_counter.current = 10
print(my_counter.current)


"""
Protected Access modifier: "_" use one underscore (You can access inside the class and subclass)
Private Access modifier: "__" use two underscore (You can only access inside the class)
"""


class Parent:
    def __init__(self):
        self._current_protected = "this is protected from the parent class"
        self.__current_private = "this is private from the parent class"

    @property
    def Current(self):
        return self.__current_private

    @Current.setter
    def Current(self, value):
        self.__current_private = value


class Child(Parent):
    def __init__(self):
        super().__init__()
        # print(self._current_protected)
        # print(self.__current_private)  # This will throw an error


my_counter = Child()

# Getter and setter
my_counter = Parent()
my_counter.Current = 10
val = my_counter.Current
