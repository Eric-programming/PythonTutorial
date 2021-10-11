# Tuple items are ordered, not changeable, allow duplicate items

# Define tuple
my_tuple = (1,)  # define 1 item
my_tuple = (1, 2, 3, 4)
my_tuple = "hello", 1, 3, 4
my_tuple = tuple([1, 2, 3, 4])


# Access Item
first_item = my_tuple[0]

# Combine tuples
my_tuple = (1, 2, 3, 4)
my_tuple += (1, 2, 3)

# Deconstruct
my_tuple = "iphone", 1399, "Vancouver"

product_name, price, location = my_tuple
