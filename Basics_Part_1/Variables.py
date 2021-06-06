"""Variables are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to variables, you can store integers, decimals or characters in these variables.
Assigning Values to Variables

Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (=) is used to assign values to variables.

The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example −"""

# snake_case
# Start with lowercase or underscore
# Letters, numbers & underscores
# Case Sensitive
# Don't overwrite keywords

user_id = 121          # Snake case
counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string
a,b,c = 1,2,3

print(user_id)
print(counter)
print(miles)
print(name)

# Augmented Assignment Operator

x = 5
x += 20
print(x)
