import sys

my_list = [1, 2, 'gyanesh', 'tiwari']

print(my_list)

first_element = my_list[0]

print(first_element)

list_len = len(my_list)

print(list_len)

my_list.append('test')

print(my_list)

my_list.remove(2)

print(my_list)

new_list = my_list + [3,4]

print(new_list)

new_list.remove('test')

print(new_list)

is_present = 'tiwari' in my_list 

if is_present:
  print("its baba")
else:
  print("someone else")