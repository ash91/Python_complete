# Python Dictionary

'''Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized.

Note – Keys in a dictionary doesn’t allows Polymorphism.

Creating a Dictionary
In Python, a Dictionary can be created by placing sequence of elements within curly {} braces, separated by ‘comma’. Dictionary holds a pair of values, one being the Key and the other corresponding pair element being its Key:value. Values in a dictionary can be of any datatype and can be duplicated, whereas keys can’t be repeated and must be immutable.

Note – Dictionary keys are case sensitive, same name but different cases of Key will be treated distinctly.'''

# dictionary = {'a': [1,2,3,4],'b':['apple', 'mango', 'grapes'],'c':['scooter','bike', 'car'],'d':{88:'icici',45:'meme'}}
# print(dictionary['d'][45])

# Keys in dictionary must be unique

# my_list = [
#     {
#         'a':[1,2,3],
#         'b':'hello',
#         'c':True
#     }, 
#     {
#         'a':[4,5,6],
#         'b':'world',
#         'c':True  
#     }
# ]
# print(my_list[0]['a'][2])
# print(my_list[1]['b'])

# Dictionary Methods

user = {

    'basket': [1,2,3],
     'greet' : 'hello'
}
# user2 = dict(name='Ashish')
# print(user.get('age' ,60))

user3 = user.copy()
# print('basket' in user.keys())
# print(user.items())
print(user.popitem())

print(user3)




