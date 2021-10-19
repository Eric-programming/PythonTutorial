# Global (Define outside of func) vs Local (Define inside of func)

my_global_str = "global"


def foo():
    print("my_global_str inside:", my_global_str)
    my_local_str = "local"
    print(my_local_str)


print(my_global_str)

foo()
# global (change global var inside function)
my_global_str = "global-2"


def foo2():
    global my_global_str
    my_global_str = "global-3"


foo2()
print(f"this my my_global_str {my_global_str}")  # expection: "global-3"

# nonlocal var (change var in nested functions)


def outer():
    my_str = "local"

    def inner():
        nonlocal my_str
        my_str = "nonlocal"
        print("inner:", my_str)

    inner()
    print("outer:", my_str)


outer()
