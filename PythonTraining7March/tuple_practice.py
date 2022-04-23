tup1 = (3, 5, 7, 8, 5, 2, 3)

"""
-> tuple is immutable data type
-> tuple follow same indexing like list and string.
-> tuple can contain any type data.
"""
"""
print(tup1)
print(type(tup1))

print(tup1[1])

print(tup1[-2])


print(tup1[2:])
#

tup2 = (3, 5, 7, 8, 5, 2, 3)
list1= []
for var in tup2:
    if var%2 == 0:
        list1.append(var**2)
    else:
        continue

print(list1)

# tuple methods.
print(dir(tup1))
"""
"""
'count', 'index'
"""
"""

tup3 = (3, 5, 7, 8, 5, 2, 3)

print(tup3.count(3))

print(tup3.index(8))

# get max number:
print("max:", max(tup3))

# get mini number:
print("mini:", min(tup3))



# get sum of all number
print("sum :", sum(tup3))

# Get max number fro, given tuple
tup4 = (3, 5, 7, 8, 5, 2, 3, 51, 23, 4)

max_num = 0
min_num = tup4[0]

for var in tup4:
    if var > max_num:
        max_num = var
    if var < min_num:  # 3, 2
        min_num = var
    print("min_val:", min_num, var)

print("max_num :", max_num)
print("min_num :", min_num)

num_sum = 0

for var in tup4:
    num_sum = num_sum + var

print("all number addition :", num_sum)
"""
##################################################################
#Program :

tup1 = ('a', 'b', 'c', 'd', 'e')
tup2 = (123, 346, 678, 342, 333)

#outpu1 = {'a': 123, 'b': 346, 'c': 678, 'd': 342, 'e': 333}
#output2 = {'AaA': 2, 'BbB': 4, 'CcC': '7', 'DdD': 4, 'EeE': 2 }
"""
output_dict = {}
for i in range(len(tup1)):
    print(i, tup1[i], tup2[i])
    output_dict[tup1[i]] = tup2[i]

print(output_dict)


output_dict2 = {}
i = 0
while i < len(tup1):
    output_dict2[tup1[i]] = tup2[i]
    
    i = i + 1
print(output_dict2)
"""
tup1 = ('a', 'b', 'c', 'd', 'e')
tup2 = (123, 346, 678, 342, 333)

#output2 = {'AaA': 2, 'BbB': 4, 'CcC': '7', 'DdD': 4, 'EeE': 3}

output2 = {}
i = 0
while i < len(tup1):
    val1 = tup1[i]
    val2 = tup2[i]
    key = f"{val1.upper()}{val1}{val1.upper()}"
    value = str(val2)[1]
    output2[key] = int(value)
    i = i+1

print(output2)

#


# Home work.
