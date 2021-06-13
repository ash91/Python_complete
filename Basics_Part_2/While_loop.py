# Python While Loop

# In Python, While Loops is used to execute a block of statements repeatedly until a given condition is satisfied. And when the condition becomes false, the line immediately after the loop in the program is executed. While loop falls under the category of indefinite iteration. Indefinite iteration means that the number of times the loop is executed isn’t specified explicitly in advance.

count = 0
while count < 50:
    print(count)
    count = count+1
else:
    print("DOne with looping")

my_list = [1, 2, 3]
for item in my_list:
    print(item)
    # break
    continue
    # pass

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue
