# Python Logical Operators with Examples

# Operators are used to perform operations on values and variables. These are the special symbols that carry out arithmetic and logical computations. The value the operator operates on is known as Operand.


# Logical operators
# In Python, Logical operators are used on conditional statements (either True or False). They perform Logical AND, Logical OR and Logical NOT operations.

# OPERATOR	DESCRIPTION	SYNTAX
# and	Logical AND: True if both the operands are true	x and y
# or	Logical OR: True if either of the operands is true	x or y
# not	Logical NOT: True if operand is false	


# Python program to demonstrate
# logical and operator
  
a = 10
b = 10
c = -10
  
if a > 0 and b > 0:
    print("The numbers are greater than 0")
  
if a > 0 and b > 0 and c > 0:
    print("The numbers are greater than 0")
else:
    print("Atleast one number is not greater than 0")



# Python program to demonstrate
# logical and operator
  
a = 10
b = 12
c = 0
  
if a and b or c:
    print("All the numbers have boolean value as True")
else:
    print("Atleast one number has boolean value as False")



is_magician = False
is_expert = False

if is_magician and is_expert:
    print("You are a master magician")
elif is_magician or is_expert:
    print("At least you're getting there")
else:
    print("You need magic power")
