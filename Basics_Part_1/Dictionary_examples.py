# Creating a Dictionary 
# with Integer Keys
Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)
  
# Creating a Dictionary 
# with Mixed keys
Dict = {'Name': 'Geeks', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

#Dictionary can also be created by the built-in function dict(). An empty dictionary can be created by just placing to curly braces{}

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Geeks', 2: 'For', 3:'Geeks'})
print("\nDictionary with the use of dict(): ")
print(Dict)
  
# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Geeks'), (2, 'For')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# Nested Dictionary:

# Creating a Nested Dictionary 
# as shown in the below image
Dict = {1: 'Geeks', 2: 'For', 
        3:{'A' : 'Welcome', 'B' : 'To', 'C' : 'Geeks'}}
  
print(Dict) 

'''Adding elements to a Dictionary
In Python Dictionary, Addition of elements can be done in multiple ways. One value at a time can be added to a Dictionary by defining value along with the key e.g. Dict[Key] = ‘Value’. Updating an existing value in a Dictionary can be done by using the built-in update() method. Nested key values can also be added to an existing Dictionary.
Note- While adding a value, if the key value already exists, the value gets updated otherwise a new Key with the value is added to the Dictionary.'''

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)
  
# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Adding set of values 
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)
  
# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)
  
# Adding Nested Key value to Dictionary
Dict[5] = {'Nested' :{'1' : 'Life', '2' : 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)

'''Accessing elements from a Dictionary
In order to access the items of a dictionary refer to its key name.Key can be used inside square brackets.'''


# Python program to demonstrate  
# accessing a element from a Dictionary 
  
# Creating a Dictionary 
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
  
# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])
  
# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])