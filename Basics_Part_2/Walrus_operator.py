# Walrus Operator in Python 3.8

# One of the latest features in Python 3.8 is the Walrus Operator. 


# Walrus-operator is another name for assignment expressions. According to the official documentation, it is a way to assign to variables within an expression using the notation NAME := expr. The Assignment expressions allow a value to be assigned to a variable, even a variable that doesn’t exist yet, in the context of expression rather than as a stand-alone statement.

a = [1, 2, 3, 4]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

a ='Hellooooooooooo'

if ((n := len(a))>10):
    print(f'Character too long {n}')

while ((n := len(a))>1):
    print(n)
    a=a[:-1]
print(a)