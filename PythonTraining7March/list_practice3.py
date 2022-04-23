"""
#28). Write a python program to check whether a list contains a sublist.

list1 = [4, 6, 8, 3, 2, 4, 2, 5, 7]
list2 = [5, 4, 3]

# Way1

temp = True
for var in list2:
    if var is not list1:
        temp = False
    else:
        continue
if temp:
    print("list2 is subset of list1")
else:
    print("list2 is not subset of list1")


# Way2

list1 = [4, 6, 8, 3, 2, 4, 2, 5, 7]
list2 = [5, 4, 1]

set1 = set(list1)
set2 = set(list2)
print(set2.issubset(set1))

#_____________________________________________

#11. Write a python program to get common elements from two list.
list1 = [4, 5, 7, 9, 2, 1]
list2 = [2, 5, 8, 3, 4, 7]
common_element = [4, 5, 7, 2]

com_list = []
for var in list1:
    if var in list2:
        com_list.append(var)
    else:
        continue

print(com_list)
"""
#_______________________________________
#12. Write a python program to re
#
#
# verse a list with for loop.

list1 = [4, 6, 2, 7, 11, 3, 8]

# Way1: reverse with for loop
output_list = []
for i in range(-1, -len(list1)-1, -1):
    output_list.append(list1[i])

print(output_list)

# Way2: reverse with reverse method.
list1 = [5, 7, 2, 1, 6, 3, 1, 15]
list1.reverse()
print(list1)

# Way3: reverse with reversed method.
list1 = [5, 7, 2, 8, 11, 12, 1, 3]
list2 = reversed(list1)
output = [elem for elem in list2]
print(output)


# Way4 : reverse list with slicing
input_list = [5, 2, 6, 1, 7, 11, 2, 45, 3]
print(input_list[::-1])

# Way5 : reverse with list with while loop.

list1 = [5, 3, 12, 5, 7, 23, 12]
index = 1
output = []
while index < len(list1)+1:
    output.append(list1[-index])
    index = index +1

print(output)






