# Encapsulation allow us to put restrictions on accessing variales/methods


class Counter:
    def __init__(self):
        self.current = 0

    def increment(self):
        self.current += 1

    def value(self):
        return self.current

    def reset(self):
        self.current = 0


my_counter = Counter()
print(my_counter.current)  # We can still access and change current outside of Counter
