# Sort using comparator
from functools import cmp_to_key
from datetime import datetime

my_list = [
    {"height": 180, "born": datetime(1997, 1, 1)},
    {"height": 185, "born": datetime(1994, 1, 1)},
    {"height": 180, "born": datetime(1999, 1, 1)},
    {"height": 179, "born": datetime(1980, 1, 1)},
]
sorted_by_height = sorted(my_list, key=lambda person: person["height"])

HEIGHT = "height"
BORN = "born"


def comparator_sorted_by_tallest_and_youngest(a, b):
    return (b[HEIGHT] - a[HEIGHT]) + ((b[BORN] - a[BORN]).days)


sorted_by_tallest_and_youngest = sorted(my_list, key=cmp_to_key(comparator_sorted_by_tallest_and_youngest))


def comparator_sorted_by_tallest_or_youngest(a, b):
    """
    Sort by tallest to shortest, but if their heights are the same
    then we are going to sort by youngest to oldest
    """
    if b[HEIGHT] > a[HEIGHT]:
        return 1  # b comes before a
    elif a[HEIGHT] > b[HEIGHT]:
        return -1  # a comes before b
    else:
        return (b[BORN] - a[BORN]).days


sorted_by_tallest_or_youngest = sorted(my_list, key=cmp_to_key(comparator_sorted_by_tallest_or_youngest))

sorted_by_shortest_or_oldest = sorted(my_list, key=cmp_to_key(comparator_sorted_by_tallest_or_youngest), reverse=True)

print(sorted_by_shortest_or_oldest)
