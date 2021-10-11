# List items are ordered, changeable, and allow duplicate values.

# Define List
my_list = [1, 2, "3"]
my_list = list(["i1", "i2", "i3"])
my_list = [1, 2] * 10

# Access / mutate item
my_list = ["i1", "i2", "i3"]
second_item = my_list[1]  # access second item
last_item = my_list[-1]  # access last item
second_last_item = my_list[-1]  # access second last item
my_list[0] = "item1"

# Insert Items
my_list.append("i4")  # O(1)
my_list.insert(0, "i0")

# Remove item in list
my_list.remove("i0")
my_list.pop()

# Check item exists
my_list = ["i1", "i2", "i3"]
is_exists = "i1" in my_list

# other operations
my_list.reverse()
my_list.sort()

# Combine lists
my_list += ["item2"]

# Sublist or slice
my_list = ["i1", "i2", "i3", "i4"]
my_list = my_list[2:]  # from index 2 to end
my_list = ["i1", "i2", "i3", "i4"]
my_list = my_list[1:3]  # from 1 to 3 but not include index 3
my_list = my_list[:1]  # from beginning to index 1


# Iterate list
my_list = ["i1", "i2", "i3", "i4"]
result = ""
for item in my_list:
    result += item + ","


# Shallow copy and Deep copy
my_list_2 = [1, 2, 3, 4]
my_list = my_list_2

is_equal = my_list is my_list_2

my_list = list(my_list_2)  # or my_list_2.copy()

is_equal = my_list is my_list_2

print(is_equal)
