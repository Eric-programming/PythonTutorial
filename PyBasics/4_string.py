# String is ordered, immutable, text representation data type

# Define
my_str = "Eric"  # Single quote or double quote
my_str = "I'm Eric"  # Single quote in double


# multiline string
my_str = """this is


 
multiline
"""

# Access item
my_str = "Eric"
first_char = my_str[0]
last_char = my_str[-1]

# Can't change character in string
# my_str[0] = 'e'

# Instead we need to convert to char array
my_str = "Eric"
char_arr = list(my_str)

# Substring is similar to list slicing

# String concat
my_str = "Eric" + " " + "Programming"

# Other string functions
my_str = "eric"
is_starts_with = my_str.startswith("er")
is_ends_with = my_str.endswith("ic")
upper_case_my_str = my_str.upper()
count_char = my_str.count("e")
my_str = "ericc"
replace_str = my_str.replace("c", "k")


# Split string by a character
my_str = "1,2,3,4,X,X"
my_list = my_str.split(",")

# list to string
my_str = "".join(my_list)

# F-string (String Format)
name = "Eric"
channel_name = "Eric Programming"
num = 2.2
my_str = f"My name is {name} and my YouTube Channel is called {channel_name}. 1 + 1.2 = {num}"

print(my_str)
