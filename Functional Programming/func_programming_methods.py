# map , filter , zip and reduce
from functools import reduce # importing reduce function
my_list = [1,2,3]
# your_list =[10,20,30]
def multiply_by2(item):
    # new_list = []
    # for item in li:
    #     new_list.append(item*2) # Normal function block
    # return new_list
    return item*2

def check_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item


# print(list(map(multiply_by2, my_list))) # Using map function
# print(list(filter(check_odd, my_list))) # Filter function
# print(list(zip(my_list, your_list)))      # Zip function
print((reduce(accumulator, my_list, 0)))
print(my_list)

# Exercise

from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()

print(list(map(capitalize, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def is_smart_student(score):
    return score > 50

print(list(filter(is_smart_student, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulator(acc, item):
    return acc + item

print(reduce(accumulator, (my_numbers + scores)))