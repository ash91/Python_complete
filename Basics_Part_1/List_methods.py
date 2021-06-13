new_list = ['apple', 'bananna', 'cheese', 'grapes', 'watermelon']
print(new_list)
new_list.insert(0, 'papaya')
new_list.reverse()
print(new_list)
print(new_list[::-1])

# # Create a range
print(list(range(1, 99)))

sentence = ','
new_sentence = '!'.join(['a', 'b', 'c', 'd'])
print(new_sentence)
new_list.pop(1)
new_list.remove('grapes')
new_list.extend(['onion', 20, 'potato', 25, 'carrot', 30])

print(new_list.index('grapes', 0, 4))
print('apple' in new_list)
added_list = new_list
print(sorted(added_list))
