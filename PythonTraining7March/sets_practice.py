set1 = {4, 6, 8, 2, 4, 6}
print(set1)

"""
-> sets is mutable data type
-> sets is a unstructure data type, it does not follow the indexing.
-> sets store only unique data.
"""
print(dir(set1))

"""
'add', 'clear', 'copy', 
'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset', 'pop', 
'remove', 'symmetric_difference',
'symmetric_difference_update', 'union',
 'update']
"""
"""
# add data to the set
set1.add(66)

print(set1)

# remove data from set.
set1.remove(8)
print(set1)

#remove data using pop method.
set2 = set()
output = set1.pop()
print("output :",  output)
print(set1)

set2.add(output)
print(set2)

# update method
set11 = {4, 6, 8, 2}
set22 = {'a', 'b', 'c', 'e'}

set11.update(set22)

print("set11:", set11 )
print("set22:", set22 )

###########################
# program : get all unique data from the list
list1 = [5, 7, 3, 2, 2, 6, 5, 8]

output = set(list1)

remove_data1 = output.pop()
print(remove_data1)
remove_data2 = output.pop()
print(remove_data2)
remove_data3 = output.remove(8)
print(remove_data3)
print("output:", list(output))

# discard method

output.discard(5)
#output.remove(4)
print(output)

# clear data from set using clear method.
output.clear()
print(output)

##############################################

set33 = {6, 7, 3, 4}

#set33.discard(5)
set33.remove(5)

print(set33)
#

seta = {'a', 'b', 'e', 'f', 'g'}
setb = {'a', 'p', 'q', 'g', 'f'}

#union of two set. :  combine two sets and remove duplicates
output = seta.union(setb)
print(output)

#difference in two set:
output2 = seta.difference(setb)
print(output2)
output3 = setb.difference(seta)
print(output3)

#intesection between two sets. : return common values between two sets.
output4 = seta.intersection(setb)
print(output4)

# frozen set: can not add or remove data from frozen set.
setp = frozenset([3, 6, 8, 2, 5, 6])
print('frozenset:', setp)
setp.add(56)
print('frozenset:', setp)
"""

# check subset of any set.
setx = {6, 7, 3, 4, 5}
sety = {6, 5}

print(sety.issubset(setx))

# superset
print(setx.issuperset(sety))

setr = {6, 7, 3, 2, (6, 3, 5, 2)}
print(setr)

for val in setr:
    print(val, type(val))



