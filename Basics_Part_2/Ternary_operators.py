# Ternary Operator in Python

# Ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false. It was added to Python in version 2.5.
# It simply allows to test a condition in a single line replacing the multiline if-else making the code compact.

# Syntax :

# [on_true] if [expression] else [on_false] 

#Simple Method to use ternary operator:

# Program to demonstrate conditional operator
a, b = 10, 20
  
# Copy value of a in min if a < b else copy b
min = a if a < b else b
  
print(min)


# SHort Circuting

is_Friend = True
is_User =False

print(is_Friend or is_User) # Here is_User is not checked because or requires any one to be True.
