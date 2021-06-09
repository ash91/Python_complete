# Tuples in Python

"""A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable."""

# Tuple are faster than list

my_tuple = (1,2,3,4,5)
print(my_tuple[1])
print(5 in my_tuple)

# user = {
#     (1,2):[1,2,3],
#     'greet':'hello'
# }
# print(user[(1,2)])

new_tuple = my_tuple[:]
print(new_tuple.count(1))