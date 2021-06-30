# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax
# lambda arguments : expression 


x = lambda a : a + 10
print(x(5)) 


x = lambda a, b : a * b
print(x(5, 6)) 

# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:

# def myfunc(n):
#   return lambda a : a * n 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

# exercise

# Square

my_list = [5,4,3]

new_list = list(map(lambda num: num **2, my_list))

print(new_list)

# List Sorting

a = [(0,2), (4,3),(10, -1), (9,7)]
a.sort(key = lambda x : x[1])
print(a)