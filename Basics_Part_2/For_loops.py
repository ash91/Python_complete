# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# This is less like the for keyword in other programming languages, and works more like an iterator method as found
# in other object-orientated programming languages.

# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.

# Iterable - List, Dictionary, Tuple,Set, String
# Iterated -> One by one check each item in the collection.
for i in [1, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    for x in ['a', 'b', 'c']:
        print(i, x)

user = {
    'name': 'ashish',
    'age': 30,
    'cant_swim': True
}

for key, value in user.items():
    print(key, value)
for item in user.keys():
    print(item)
for item in user.values():
    print(item)


# Counter Exercise

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
for items in my_list:
    count = count+items
print(count)

for number in range(10, 0, -2):
    print(number)

# Enumerate

for i, char in enumerate((list(range(100, 0, -2)))):
    if char == 50:
        print(f'Index of 50 is: {i}')
