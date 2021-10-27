# map(), filter(), and reduce()
from functools import reduce

# map()
my_list = [1, 2, 3, 4]
my_list = list(map(lambda num: num * num, my_list))

# Option 2 not use map()
my_list = [1, 2, 3, 4]
my_list = [num * num for num in my_list]

# filter()
my_list = [1, 2, 3, 4]
my_even_list = list(filter(lambda x: x % 2 == 0, my_list))

# Option 2 not to use filter()
my_even_list = [num for num in my_list if num % 2 == 0]


# reduce()
my_list = [1, 2, 3, 4]

sum = 0
for num in my_list:
    sum += num

result_with_reduce = reduce(lambda sum, cur_num: sum + cur_num, my_list)
