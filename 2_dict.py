# Dictionary is a key-value pairs, unordered, and changeable

# Define
my_dict = {}
my_dict = dict()

# Insert/Remove
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict[1] = 1
my_dict.popitem()  # pop the last item that was inserted
my_dict[1] = 1
del my_dict[1]
my_dict[(1, 2)] = "1,2"

# Combine Dicts
my_dict = {"brand": "Ford", "model": "Mustang", "year": 1964}
my_dict_2 = {"brand": "Ford", "model": "GT", "year": 2009, 1: 1}
my_dict.update(my_dict_2)

# Check existance
is_exists = 1 in my_dict
is_exists = "brand" in my_dict

# Iteration
output = "Iterating keys: "
for key in my_dict.keys():
    output += key + " "
print(output)

output = "Iterating value: "
for value in my_dict.values():
    output += str(value) + " "
print(output)

output = "Iterating items: "
for key, value in my_dict.items():
    output += "(" + str(key) + "," + str(value) + ") "
print(output)
