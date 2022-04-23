"""
data type conversion
"""
#1 Interger

#-> Int -> float
"""
num1 = 30
num2 = float(num1)
print(type(num2))
print(num2)
"""
# int -> string
"""
num3 = 400
str_output = str(num3)
print(type(str_output))
print(str_output)
"""

# int -> list : not allowed
"""
num3 = 500
list_output = list(num3)
print(type(list_output))
"""

# int -> tuple : not allowed
# int -> dict : not allowed
# int -> set : not allowed
"""
num1 = 567
#print(set(num1))
# int -> boolean : Allowed
print(bool(num1))
"""
#######################################################
#2) Float

# float -> int
"""
num2 = 4.5
output = int(num2)
print(type(output))
print(output)
"""
# float -> string
"""
num3 = 40.5
output = str(num3)
print(type(output), output)
"""
# float -> list : not allowed
# float -> tuple : not allowed
# float -> dict : now allowed
# float -> set : not allowed
# float -> boolean
"""
num4 = -80.6
output = bool(num4)
print(type(output), output)
"""
########################################################
#3  String

#string -> int

# this is not allowed
#str1 = "Hello"
# output = int(str1)
# print(type(output), output)

""""
str2 = '567845'

print(type(str2))
output = int(str2)
print(type(output), output)

# string to float
output2 = float(str2)
print(type(output2), output2)
"""

# string -> list
"""
str3 = 'Hello'
output = list(str3)
print(type(output), output)

# string -> tuple

output2 = tuple(str3)
print(type(output2), output2)
"""
# string -> dict

# it is not allowed
"""
str4 = "Good Morning"
output = dict(str4)
print(type(output), output)

str5 = "{'a' : 'abc', 'b' : 'pqr'}"
output = dict(str5)
print(type(output), output)
"""

# string -> set
"""
str5 = "Python Hello"
output = set(str5)
print(type(output), output)
# <class 'set'> {'h', 'P', ' ', 'e', 'l', 'y', 't', 'o', 'H', 'n'}
"""
"""
# string -> boolean
str6 = ""
output = bool(str6)
print(type(output), output)
"""
#############################################################

# 4) List

# list -> int : not allowed

"""
list1 = [1, 5, 7]
output = int(list1)
print(output)
"""

# list -> float : not allowed
# list -> string
"""
list1 = [4, 6, 8]
output_str = str(list1)
print(type(output_str), output_str)

print(list1[0])
print(output_str[0])
"""
# list -> tuple

list2 = [5, 7, 8, 'hello']
tup1 = tuple(list2)
print(type(tup1), tup1)

val1 = list2[0]
print(val1)
val = tup1[3]
print(val)
print(type(val))

# list -> dict : not allowed
# list -> set
"""
list1 = [4, 6, 2, 5, 6, 4]

set_output = set(list1)
print(set_output, type(set_output))
# {2, 4, 5, 6} <class 'set'>
"""
# list -> boolean
"""
list1 = []
output = bool(list1)
print(output, type(output))
"""
"""
list1 = ['5', 7, 8]
output = int(list1[0])
print(output, type(output))
"""

############################################
#5) Tuple

#tuple -> int : not allowed
#tuple -> float : not allowed
#tuple -> string
"""
tup1 = (5, 6, 7)
output = str(tup1)
print(output, type(output))

#tuple -> list
output2 = list(tup1)
print(output2, type(output2))

#tuple -> dict : not allowed
#tuple -> set

tup2 = (5, 6, 7, 6, 7, 4)
output3 = set(tup2)
print(output3)

# tuple -> boolean
tup3 = (5, 7, 8)
output4 = bool(tup3)
print(output4, type(output4))
"""

#################################################
# 6) Dictionary

# dict -> int : not allowed
# dict -> float : not allowed
# dict -> list : not allowed
# dict -> tuple : not allowed
# dict -> string
"""
dict1 = {'name' : 'John', 'age' : 45, 12 : 'Hello', (4, 6, 7, 7) : [4, 6, 7], 'name': 'Harry'}
print(dict1)

output = str(dict1)
print(output, type(output))
print(output[0])
print(output[1])

# dict -> set
output2 = set(dict1)
print(output2, type(output2))

# dict -> boolean
dict1 = {'a': 123}
output3 = bool(dict1)
print(output3, type(output3))
"""
##################################################
#7) Set
# set -> int : not allowed
# set -> float : not allowed
# set -> string
"""
set1 = {'a', 'b', 56, 43, 40}
output = str(set1)
print(output, type(output))

# set -> list
output3 = list(set1)
print(output3, type(output3))

# set -> tuple
output4 = tuple(set1)
print(output4, type(output4))

# set -> dict : not allowed
set1 = {5, 7, 3, 8}
output5 = dict(set1)
print(output5, type(output5))
"""
# set -> boolean
"""
set1 = {}
output = bool(set1)
print(output, type(output))
"""
###################################################
#8) Boolean

# Boolean -> int
"""
var = False
print(type(var))
output = int(var)
print(output, type(output))
"""
# Bool -> float
"""
var = False
output = float(var)
print(output, type(output))
"""

# Bool -> string
"""
var = True
output = str(var)
print(output, type(output))
print(output[0])
"""

# Bool -> list
"""
var = True
output = list(var)
print(output, type(output))
"""
# Bool -> tuple : not allowed
# Bool -> dict : not allowed
# Bool -> set : not allowed
"""
var = True
output = set(var)
print(output, type(output))
"""


