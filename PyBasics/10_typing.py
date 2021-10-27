"""
Type Hints & Annotation
Benefits:
- Better documentation
- Better Autocomplete and linting check
"""
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union

# Type Hint in variables
my_str: int = 1


def sum(a: int, b: int) -> int:
    return a + b


print(sum(1, 2))


my_list: List[List[int]] = [[1, 2, 3, 4]]
my_tuple: Tuple[int, int, int] = (
    1,
    2,
    3,
)
my_dict: Dict[str, int] = {"key": 1}
my_set: Set[str] = {"value"}


# Class type
class Car:
    pass


my_car: Car = Car()

# type Optional or Union
my_val: Optional[str] = None  # or Union[str, None]
my_val = "my string"

my_val_2: Union[str, int, bool, None] = None
my_val_2 = False
my_val_2 = 0


# type Any
my_val_3: Any = True
my_val_3 = my_car
my_val_3 = None


# type Callable
def callable_func(a: int, b: str) -> str:
    return f"{a} {b}"


def call_callable_func(func: Callable[[int, str], str]) -> str:
    return func(1, "day")
