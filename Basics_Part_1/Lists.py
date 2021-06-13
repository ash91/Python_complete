'''Lists are just like dynamic sized arrays, declared in other languages (vector in C++ and ArrayList in Java). Lists need not be homogeneous always which makes it a most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.

List in Python are ordered and have a definite count. The elements in a list are indexed according to a definite sequence and the indexing of a list is done with 0 being the first index. Each element in the list has its definite place in the list, which allows duplicating of elements in the list, with each element having its own distinct place and credibility.

Note- Lists are a useful tool for preserving a sequence of data and further iterating over it.'''

'''Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:'''

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List casn hold multiple data types
# List items are indexed, the first item has index [0], the second item has index [1] etc.

thislist = ["apple", "banana", "cherry"]
print(thislist)

li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2, 'a', True]

# List SLicing

amazon_cart = ['notebooks', 'watches', 'computer', 'television', 'furniture']

print(amazon_cart[:1:-1])

# List are mutable

amazon_cart[0] = 'Laptop'
# WHen we do list slicing it copies contents of list and in this line content of amazon_cart is copied to new_cart
new_cart = amazon_cart[:]
# new_cart = amazon_cart # We are Assigning contenets of amazon_cart which are in memeory to new_cart
new_cart[0] = 'Chair'
print(new_cart)
print(amazon_cart)
