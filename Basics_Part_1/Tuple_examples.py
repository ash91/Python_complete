#Creating Tuples


# An empty tuple
empty_tuple = ()
print (empty_tuple)


# Creating non-empty tuples
  
# One way of creation
tup = 'python', 'geeks'
print(tup)
  
# Another for doing the same
tup = ('python', 'geeks')
print(tup)

Concatenation of Tuples


# Code for concatenating 2 tuples
  
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
  
# Concatenating above two
print(tuple1 + tuple2)

Nesting of Tuples


# Code for creating nested tuples
  
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)

# Code to create a tuple with repetition
  
tuple3 = ('python',)*3
print(tuple3)


#code to test that tuples are immutable
  
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)

# Slicing in Tuples


# code to test slicing
  
tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])


# Code for deleting a tuple
  
tuple3 = ( 0, 1)
del tuple3
print(tuple3)

