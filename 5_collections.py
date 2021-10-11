# Collections module implements special container datatypes
from collections import Counter, OrderedDict, deque

# Counter (Count items)
my_str = "abcabca"
my_counter = Counter(my_str)  # {a:3, b:2, c:2} => (dict)
most_common_item = my_counter.most_common(1)  # (a,3)

my_list = [1, 1, 2, 2, 3, 1]
my_counter = Counter(my_list)  # {1:3, 2:2, 3:1} => (dict)
most_common_item = my_counter.most_common(1)  # (1,3)

# OrderedDict (Know the order of insertion)
ordered_dict = OrderedDict()
ordered_dict[3] = 1
ordered_dict[2] = 1
ordered_dict[1] = 1

my_ordered_list = list(ordered_dict.items())  # option 2: dict.popitem() pop the last item that was inserted


# Deque
my_deque = deque([1, 2])
my_deque.append(3)  # append right O(1)
my_deque.appendleft(0)  # append left O(1)
my_deque.popleft()  # pop first item O(1)
my_deque.pop()  # pop first item O(1)

my_deque.extend([3, 4])
my_deque.extendleft([-1, 0])

print(my_deque)
