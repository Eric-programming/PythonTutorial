# Argument vs parameter
def square_value(num):
    return num * num  # num = parameter


result = square_value(2)  # 2 is the argument for square_value function

# keyword argument
def order_func(a, b, c):
    return f"a is {a}, b is {b}, c is {c}"


result = order_func(c=1, b=2, a=3)  # Order doesn't matter
# order_func(c=1, b=2, 3) is not allowed


# *args vs **kwargs (variable-length arguments)


def foo(a, b, *args, **kwargs):
    print(a, b)

    # args is a tuple
    for arg in args:
        print(arg)

    # kwargs (keyword arguments) is a dict
    for key, value in kwargs.items():
        key_value_pair = (key, value)
        print(key_value_pair)


foo(1, 2, 11, 12, name="eric", channel="programming")
print("hello")

# unpacking list/tuple into function arguments
def foo2(a, b):
    return f"{a}, {b}"


my_list = [1, 2]
result = foo2(*my_list)  # length of the list matters

my_tuple = (1, 2)
result = foo2(*my_tuple)  # length of the tuple matters

my_dict = {"a": 1, "b": 2}
result = foo2(**my_dict)  # key must match the parameter name
