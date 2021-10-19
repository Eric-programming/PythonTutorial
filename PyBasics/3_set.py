# Set items are ordered, mutable, no duplicates

# Define
my_set = {}
my_set = set()

# Insert/Remove
my_set = {1, 2, 3, 4, 4}
my_set.add(5)
my_set.remove(1)
pair = (1, 2)
my_set.add(pair)

# Check existance
is_exists = (1, 2) in my_set
is_exists = pair in my_set

# Combine/compare sets without duplicates
my_set = {1, 2, 3}
my_set_2 = {3, 4, 5}
union_set = my_set.union(my_set_2)
intersection_set = my_set.intersection(my_set_2)
diff_set = my_set.difference(my_set_2)
my_set.update(my_set_2)


# Iteration
my_set = {1, 2, 3}
output = "Iterating set's values: "
for value in my_set:
    output += str(value) + " "
print(output)
