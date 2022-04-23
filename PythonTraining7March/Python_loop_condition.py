#print(1)
#print(2)
#print(3)
#.
#.
#print(10)

# range(initial, endpoint, difference)
"""
for var in range(1, 10, 1)
    print(var)

"""
# in loop with range method, last value always going to skip
# for var in range(1, 11, 3):
#     print(var)

# if difference is not set, then default value is 1
# for var in range(1, 10):
#     print(var)

# if initial value is not set, then default initial value is 0
# for var in range(10):
#     print(var)


# num = int(input("Please enter your number :"))
# for var in range(1, 11):
#     print(num, "*", var, "=", var*num)

# for i in range(1, 10):
#     #print(i, end=",")
#     print(i, ":", i**3)

# get all the even numbers from 1 to 20
"""
for i in range(1, 20):
    if i%2 == 0:
        print(i)
"""
# get all the number which are divisible by 2 & 3 from 1 to 50

"""
for i in range(1, 50):
    if i%2 == 0 and i%3 == 0:
        print(i)
"""
"""
# get data from list
list1 = [2, 5, 7, 9, 3]

for var in list1:
    print(var)

print("_"*30)
list_length = len(list1)
print("length :", list_length)

for i in range(list_length):
    print(i, ":", list1[i])

print("_"*30)
# Get max number from the list

max_num = 0

for var in list1:
    if var > max_num:
        max_num = var
print("max_num :", max_num)


print("_"*30)
list2 = [2, 5, 7, 9, 3, 23, 6, 2, 22]
max_num1 = list2[0]

for i in range(len(list2)):
    #print(i)
    # i = 0, 1, 2
    if list2[i] > max_num1:
        max_num1 = list2[i]

print("max_num :", max_num1)
"""
"""

str1 = "Hello Good Morning"

"""
# HH
# ee
# .
# .
"""
str2 = "aeiou"

# print all vowels only
for var in str1:
    #print(var*2)
    if var in str2:
        print(var)
"""

######################################
#Nested Loop

"""
for i in range(3):
    for j in range(2):
        print(i, ":", j)
        
output :
i = 0 , j : 0, 1
i = 1 , j : 0, 1
i = 2 , j : 0, 1

"""

for i in range(5):
    for j in range(3):
        print("address :",i ,"package :", j)
    print("####"*10)

"""
*
* *
* * *
* * * *
* * * * *
"""

# Practice Program :

num1 = 456
# list of number which can divide 3
# list of number which can divide 5 and 7
# list of number which can divide 11









































