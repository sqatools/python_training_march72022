
"""
dict1 = {'name' : 'rohan', 'age': 40, 'addrees': 'Pune'}

# get All Keys
keys_data = dict1.keys()
print(keys_data)
list1 = list(keys_data)
print(list1[0])

# Get all values
values_data = dict1.values()
print(values_data)

list2 = list(values_data)
print(list2[2])


# Program : store all keys and values of the dict in two different list
dict1 = {'name' : 'rohan', 'age': 40, 'addrees': 'Pune', 'email' : 'pytest@test.com'}
key_list = []
value_list = []

for key ,value in dict1.items():
    key_list.append(key)
    value_list.append(value)

print(value_list)
print(key_list)

# has_key method.

#dict1.get()
#print(dict1.has_key('name'))

result = True if 'name1' in dict1 else False
print(result)

# update method

dict1 = {'a' : 1, 'b' : 34, 'c': 2, 'd': 12}
dict2 = {'c' : 1, 'd' : 34, 'e': 2, 'f': 12}

dict2.update(dict1)
print(dict2)

print("*"*20)
# dict3 = dict1 + dict2
# print(dict3)

dict4 = "{'a': 2}" + "{'b': 3}"
print(dict4)

# deep copy and shallow copy

dict1 = {'abc': 123, 'pqr': 456}

dict2 = dict1

dict2['xyz'] = 567

print(dict2)
print(dict1)

# deep copy
dict4 = {'abc': 123, 'pqr': 456}
dict3 = dict4.copy()

dict3['name'] = 'Rohit'

print(dict3)
print(dict4)

#############################
dictp = {'abc': 123, 'pqr': 456, 'xyz' : 345, 'gef': 342}


output = [item[0] for item in dictp.items() if item[1]%2 == 0]
print(output)
"""

##################################################################
"""
#program :
list1 = [3, 6, 8, 2, 7, 3, 5, 3, 5, 2, 4]
#output = {3: 3, 6 : 1, 8:1, 7:1, 5:2, 2:2, 4: 1}

result_dict = {}

for var in list1:
    if var in result_dict:
        result_dict[var] += 1
    else:
        result_dict[var] = 1

print(result_dict)

result_dict2  = {}

for var in list1:
    if var not in result_dict2:
        var_count = list1.count(var)
        result_dict2[var] = var_count
    else:
        continue

print(result_dict2)
"""
###################################################
# program :
#dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language'}

#output1 = {'a': 'HeLlO', 'b': 'PyThOn', 'c': 'PrOgRaMmInG', 'd': 'LaNgUaGe'}
#output2 = {'a': 'lll', 'b': 'hhh', 'c': 'iii', 'd': 'aaa'}
#output3 = {'a': 'Hjljo', 'b': 'Pjtjoj', 'c': 'Pjojrjmjijg', 'd': 'ljnjujgj'}
#output4 = {'a': 'H_e_l_l_o', 'b': 'P-y-t-h-o-n', 'c': 'P*r*o*g*r*a*m*m*i*n*g', 'd': 'l%a%n%g%u%a%g%e'}
#output5 = {'a' : 'lohe', 'b': 'onPy', 'c': 'ngPr', 'd': 'gela'}

# Program1 =

dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language'}
#output1 = {'a': 'HeLlO', 'b': 'PyThOn', 'c': 'PrOgRaMmInG', 'd': 'LaNgUaGe'}

"""
step1 : output_dict ={}
step2 : Iterate through each data using loop. for key, val in dict1.items()
step3 : Iterate through each char of string of string using for i in range(len(val))
step4 : if i%2 == 0:
            char = val[i].upper()
        else:
            char = val[i].lower
        new_str = new_str + char
step5 : add new new string in output dictionary.
step6 : print output dictionary.
"""
"""
output_dict = {}
for key, val in dict1.items():
    new_str = ''
    for i in range(len(val)):
        if i%2 == 0:
            char = val[i].upper()
        else:
            char = val[i].lower()
        new_str = new_str + char

    output_dict[key] = new_str

print(dict1)
print(output_dict)
"""
#___________________________________________________________________________

"""
# Program2
dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language'}
#output2 = {'a': 'lll', 'b': 'hhh', 'c': 'iii', 'd': 'aaa'}

output_dict = {}
for key, val in dict1.items():
    last_third = val[-3]
    output_dict[key] = last_third*3

print(dict1)
print(output_dict)
"""

#Program3
#dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language'}
#output3 = {'a': 'Hjljo', 'b': 'Pjtjoj', 'c': 'Pjojrjmjijg', 'd': 'ljnjujgj'}
"""
step1 : output_dict = {}
step2 : apply loop on dict and get key and value.
step3 : apply loop on string using range for i in range(len(val))
step4 : if i%2 = 0: new_str = new_str + char else  new_str = new_str + j
step5 : add new_str in output dict.
"""
"""
dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language', 'e': 234}

output_dict = {}
replace_char = 'j'
for key, val in dict1.items():
    new_str = ''
    if type(val) == type(str()):
        for i in range(len(str(val))):
            if  i%2 == 0:
                new_str = new_str + str(val)[i]
            else:
                new_str = new_str + replace_char
        output_dict[key] = new_str
    else:
        output_dict[key] = val

print(dict1)
print(output_dict)
"""

# Program4:
#dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language'}
#output4 = {'a': 'H_e_l_l_o', 'b': 'P-y-t-h-o-n', 'c': 'P*r*o*g*r*a*m*m*i*n*g', 'd': 'l%a%n%g%u%a%g%e'}

#str1 = 'Hello'
#print('%'.join(str1))

"""
step1:  output_dict = {}
step2:  apply loop on dict and get key and value for key, val in dict1.items()
step3 : for char in val and add in temp_str
step4 : check key data and apply additional char or special char.
step5:  then add temp string output_dict.
"""

"""
output_dict = {}

for key, val in dict1.items():
    special_char = ''
    if key == 'a':
        special_char = '_'
    elif key == 'b':
        special_char = '-'
    elif key == 'c':
        special_char = '*'
    elif key == 'd':
        special_char = '%'
    temp_str = ''
    for i in range(len(val)):
        if i == 0:
            temp_str = temp_str + val[i]
        else:
            temp_str = temp_str + special_char+ val[i]
            
    output_dict[key] = temp_str

print(dict1)
print(output_dict)
"""

output_dict = {}

for key, val in dict1.items():
    special_char = ''
    if key == 'a':
        special_char = '_'
    elif key == 'b':
        special_char = '-'
    elif key == 'c':
        special_char = '*'
    elif key == 'd':
        special_char = '%'
    output_dict[key] = special_char.join(val)

print(dict1)
print(output_dict)



###########################################################
#Program5
dict1 = {'a' : 'Hello', 'b': 'Python', 'c': 'Programming', 'd': 'language'}
#output5 = {'a' : 'loHe', 'b': 'onPy', 'c': 'ngPr', 'd': 'gela'}
str1 = 'Hello'
print(str1[-2:])
print(str1[:2])

output_dict = {}
for key , val in dict1.items():
    output_dict[key] = val[-2:] + val[:2]

print(dict1)
print(output_dict)




