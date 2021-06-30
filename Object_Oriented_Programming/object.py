# Python Classes and Objects

#     Difficulty Level : Easy
#     Last Updated : 10 Jun, 2021

# A class is a user-defined blueprint or prototype from which objects are created. Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by their class) for modifying their state.

# To understand the need for creating a class let’s consider an example, let’s say you wanted to track the number of dogs that may have different attributes like breed, age. If a list is used, the first element could be the dog’s breed while the second element could represent its age. Let’s suppose there are 100 different dogs, then how would you know which element is supposed to be which? What if you wanted to add other properties to these dogs? This lacks organization and it’s the exact need for classes. 

# Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class. A class is like a blueprint for an object.

# Some points on Python class:  

#     Classes are created by keyword class.
#     Attributes are the variables that belong to a class.
#     Attributes are always public and can be accessed using the dot (.) operator. Eg.: Myclass.Myattribute


# Class Definition Syntax:

# class ClassName:
#     # Statement-1
#     .
#     .
#     .
#     # Statement-N

class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name , age):
        self.name = name
        self.age = age

player1 = PlayerCharacter('Ashish', 30)
player2 = PlayerCharacter('Sachin', 43)

print(player1.name)
print(player2.name)

# Example

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instantiate the Cat object with 3 cats
peanut = Cat("Peanut", 3)
garfield = Cat("Garfield", 5)
snickers = Cat("Snickers", 1)


# Find the oldest cat
def get_oldest_cat(*args):
    return max(args)


# Output
print(f"The oldest cat is {get_oldest_cat(peanut.age, garfield.age, snickers.age)} years old.")