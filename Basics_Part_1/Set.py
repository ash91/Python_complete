# Sets in Python

'''A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements. Python’s set class represents the mathematical notion of a set. The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes like we do in lists.'''

my_set = {1, 2, 3, 4, 5, 5}
my_set.add(100)
my_set.add(7)
print(my_set)

# Converting List into set

my_list = [1, 2, 3, 4, 5, 5, 6, 6]
print(set(my_list))

# Sets does not support slicing

print(list(my_set))

# Sets Methods

# Method	                                    Description
# add()	                                        Adds an element to the set
# clear()	                                    Removes all the elements from the set
# copy()	                                    Returns a copy of the set
# difference()                                  Returns a set containing the difference between two or more sets
# difference_update()                           Removes the items in this set that are also included in another, specified set
# discard()	                                    Remove the specified item
# intersection()	                            Returns a set, that is the intersection of two other sets
# intersection_update()	                        Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()                                  Returns whether two sets have a intersection or not
# issubset()	                                Returns whether another set contains this set or not
# issuperset()	                                Returns whether this set contains another set or not
# pop()	                                        Removes an element from the set
# remove()                                  	Removes the specified element
# symmetric_difference()	                    Returns a set with the symmetric differences of two sets
# symmetric_difference_update()                 inserts the symmetric differences from this set and another
# union()	                                    Return a set containing the union of sets
# update()	                                    Update the set with another set, or any other iterable

my_new_set = {1, 2, 3, 4, 5}
second_set = {4, 5, 6, 7, 8, 9, 10}

# print(my_new_set.difference(second_set))
# print(my_new_set.discard(5))
# print(my_new_set)

# my_new_set.difference_update(second_set)
# print(my_new_set)

# print(my_new_set.intersection(second_set))

# Union method eg

print(my_new_set.union(second_set))
print(my_new_set | second_set)
