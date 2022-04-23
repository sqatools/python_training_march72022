dict1 = {'a': 2, 'b': 4}

"""
-> Dictionary is mutable data type.
-> Dictionary is un-structure data type, it does not follow any indexing.
-> Dict contains on unique key, its means duplicate key is not allowed.
-> Only immutable data type can be a key in the dictionary e.g int, string, tuple
-> Any type of data can be a value in the dictionary.
"""
"""
print(dict1)
print(type(dict1))

# Get key value from dict
var = dict1['a']
print(var)

# add some data to the dict.

dict1['c']  = 'Hello'
dict1['d'] = [4, 5, 6]
dict1['e'] = [7, 8, 9]

print(dict1)

print(dir(dict))
"""
"""
Methods for dict

'clear', 'copy', 'fromkeys', 'get', 
'items', 'keys', 'pop', 'popitem', 
'setdefault', 'update', 'values'
"""
"""
dict2 = {'a': 2, 'b': 4, 'c': 'Hello', 'd': [4, 5, 6], 'e': [7, 8, 9]}

output = dict2.items()
print(output)

for key, value in dict2.items():
    print("Key: ", key, "value:", value)



# remove data from the dictwith key
item = dict2.pop('a')
print("item", item)

print(dict2)


item2 = dict2.popitem()
print("item2 :", item2)
print(dict2)

#porgram : remove data from dict1 and move to dict2:
input_dict = {'b': 4, 'c': 'Hello', 'd': [4, 5, 6], 'e': [7, 8, 9]}
copy_dict = input_dict.copy()
output_dict = {}

for key, value in copy_dict.items():
    remove_value = input_dict.pop(key)
    output_dict[key] = remove_value

print("Input dict :", input_dict)
print("output dict :", output_dict)
"""
# program : verify given data if available in the dictionary or not
"""
input_dict = {'b': 4, 'c': 'Hello', 'd': [4, 5, 6], 'e': [7, 8, 9], 'name': 'john'}
user_data = 'Hello'

flag = False
for key, value in input_dict.items():
    if user_data == value:
        flag = True
        print(f"user data : {user_data} is available with key : {key}")
        break
    else:
        continue

if not flag:
    print("data is not available")

# Check specific key is available in the dictionary or not.

if 'name1' in input_dict:
    print("key is available")
else:
    print("Key is not available")

key = 'name'
output = True if key in input_dict else False
print(output, key)


# it will print all the keys from the dictionary
for data in input_dict:
    print(data)
"""

input_dict ={
    'std1' : [
    {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 50}
],
'std2' : [
    {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 55}
],
'std3' : [
    {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 45}
],
'std4' : [
    {'hindi' : 30}, {'math' : 20}, {'science': 60}, {'english' : 70}
]
}

# get stud4 english marks

print(input_dict['std4'][3]['english'])


student_db ={
    'class' : [{ '10th':[ {'std1' : [
                                {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 50}
                            ],
                    'std2' : [
                        {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 55}
                    ],
                    'std3' : [
                        {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 45}
                    ],
                    'std4' : [
                        {'hindi' : 30}, {'math' : 20}, {'science': 60}, {'english' : 70}
                    ]}]
                },
             { '11th':[ {'std1' : [
                                {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 50}
                            ],
                    'std2' : [
                        {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 55}
                    ],
                    'std3' : [
                        {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 45}
                    ],
                    'std4' : [
                        {'hindi' : 30}, {'math' : 20}, {'science': 60}, {'english' : 70}
                    ]}]
                },
            { '12th':[ {'std1' : [
                                {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 50}
                            ],
                    'std2' : [
                        {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 55}
                    ],
                    'std3' : [
                        {'hindi' : 30}, {'math' : 50}, {'science': 60}, {'english' : 45}
                    ],
                    'std4' : [
                        {'hindi' : 30}, {'math' : 20}, {'science': 60}, {'english' : 70}
                    ]}]
                }
    ]
}

print(student_db['class'][2]['12th'][0]['std2'][2]['science'])