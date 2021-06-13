# *args

# The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function. It is used to pass a non-key worded, variable-length argument list. 

# The syntax is to use the symbol * to take in a variable number of arguments; by convention, it is often used with the word args.
# What *args allows you to do is take in more arguments than the number of formal arguments that you previously defined. With *args, any number of extra arguments can be tacked on to your current formal parameters (including zero extra arguments).
# For example : we want to make a multiply function that takes any number of arguments and able to multiply them all together. It can be done using *args.
# Using the *, the variable that we associate with the * becomes an iterable meaning you can do things like iterate over it, run some higher-order functions such as map and filter, etc.
 
# **kwargs

# The special syntax **kwargs in function definitions in python is used to pass a keyworded, variable-length argument list. We use the name kwargs with the double star. The reason is because the double star allows us to pass through keyword arguments (and any number of them).



# A keyword argument is where you provide a name to the variable as you pass it into the function.
# One can think of the kwargs as being a dictionary that maps each keyword to the value that we pass alongside it. That is why when we iterate over the kwargs there doesn’t seem to be any order in which they were printed out.

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, num1=5, num2=10))

# Exercise

def highest_even(li):
    evens =[]
    for i in li:
        if i % 2 == 0:
            evens.append(i)
    return max(evens)
print(highest_even([10,2,3,4,5,6,8,12]))

