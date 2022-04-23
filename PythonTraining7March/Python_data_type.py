"""
Python data type
1. Numeric
        a). Integer
        b). Float
2. Sequence
        a). String
        b). List
        c). Tuple
3. Dictionary
4. Set
5. Boolean
"""
"""
# 1) Numeric
a = 123
b = 444455555555555
c = 3.200000005555

print(a)
print(type(a))

print(a+b)

d = a + c
print(d)
print(type(d))
"""
# 2) Sequence :

# a) String :

#+ index    0 1 2 3 4 5 6 7 8 9 10
#   str1 = "G o o d M o r n i n g"
#- index  -11-10-9-8-7-6-5-4-3-2-1
"""
str1 = "Good Morning"
str2 = 'Hello'


print(type(str1))
print(type(str2))
print(type(str3))

print(str1[0])
print(str1[-1])
"""
"""
# b) list:

# List is mutable data type
#        0     1     2     3
list1 = [12, 'abc', 3.4, True]
#        -4    -3    -2   -1
print(type(list1))
print(list1[2])
print(type(list1[2]))
var1 = list1[-3]

print(var1)
print(type(list1[1]))
"""
"""
# c) Tuple
# Tuple Immutable data type
#        0   1     2      3
tup1 = (456, 78, "Hello", 4.6)
#       -4   -3   -2     -1

print(type(tup1))

data1 = tup1[1]
print(data1)

data2 = tup1[-2]
print(data2)

print(tup1)
"""
#######################################################

#3) Dictionary
# in dict all keys should be unique.
# dict is un-structure data type
# Key should be a immutable data type, int, float, string, tuple
# list can not be a key in the dict
# we can store any type of data as value
dict1 = {'name' : 'Aditya', 'email': 'adi@gmail.com', 'mobile': 34567}
dict2 = {123: 'a', (4, 5, 6) : 234, 'details' : {'st': 'st01', 'name': 'rahul'}}


print(dict1)
print(type(dict1))
mobile = dict1['mobile']
print(mobile)

print(dict2)
print(dict2[(4, 5, 6)])

print(dict2['details'])
print(dict2['details']['name'])
print(dict2['details']['name'][2])

# Get all keys
#keys_data = dict2.keys()
#print(type(keys_data))
#list1 = list(keys_data)

#####################################
#4) Sets :
# -> set is does not follow any indexing
# -> set store unique data, duplicate data is not allowed.
# -> Mutable data type, we can add remove data from sets.

set1= {4, 6, 'a', 4, (2, 4, 5)}
print(set1)

#5) Boolean : True and False is consider under boolean data type
# == equal to operator
a = 20
b = 20
print(a == b)















