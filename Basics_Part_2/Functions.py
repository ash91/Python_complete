# Functions

'''
A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

As you already know, Python gives you many built-in functions like print(), etc. but you can also create your own functions. These functions are called user-defined functions.

Defining a Function
You can define functions to provide the required functionality. Here are simple rules to define a function in Python.

Function blocks begin with the keyword def followed by the function name and parentheses ( ( ) ).

Any input parameters or arguments should be placed within these parentheses. You can also define parameters inside these parentheses.

The first statement of a function can be an optional statement - the documentation string of the function or docstring.

The code block within every function starts with a colon (:) and is indented.

The statement return [expression] exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return None.

Syntax
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression] '''

#Parameters & Arguments
# Parameters are used when we define a function and Arguments are used when we call a function.
# Positional parameter and Arguments


def say_hello(name, city):  # These are function parameters
    print(f"hello {name} are you from {city}")


say_hello('ashish', 'hyderabad')  # These are arguments


# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,1,1,1,1,1,0],
#   [0,0,1,1,1,0,0],
#   [0,0,0,1,0,0,0]
# ]
# # Iterate over picture.
# def show_shape():
#     for image in picture:
#         for pixel in image:
#             if (pixel ==1):
#                 print('*', end='')
#             else:
#                 print(' ', end='')
#         print('')
# show_shape()
# show_shape()
# show_shape()
# show_shape()
