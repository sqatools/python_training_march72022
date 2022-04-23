
"""
# deep copy and shallow copy

# shallow copy
list1 = [3, 5, 7, 2]

list2 = list1

list2.append(34)

print("list1 :", list1)
print("list2 :", list2)

# Deep copy

lista = [2, 5, 3, 8, 4]
listb = lista.copy()

listb.append(55)

print("lista:", lista)
print("listb:", listb)

##############################################################

listp = [5, 7, 8]
listq = [4, 7, 2]

listr = listp + listq
lists = listr
listt = lists
lists.append(60)

listu = lists.copy()

listu.append(50)

print("listt : ", listt, id(listt))
print("lists :", lists, id(lists))
print("listu :", listu, id(listu))
"""

"""
# list comprehension.

list1 = [2, 6, 8, 9, 11, 17, 19, 20]
output = []

for val in list1:
    if val%2 == 0:
        output.append(val**2)
    else:
        continue
print(output)

# simple list comprehension with loop
result = [x**2 for x in list1]
print(result)

# list comprehension with if condition
result2= [x**2 for x in list1 if x%2 ==0]
print(result2)

# list comprehension with if else condition
result3 = [("even", x) if x%2==0 else ("odd", x) for x in list1]
result4 = [{x:"even"} if x%2==0 else {x:"odd"} for x in list1]
print("result3 :", result3)
print("result4 :", result4)


"""

a =[-1,-15,-4,5,7,-50,-28,9,-8,4,-9,-70]
b = a.copy()

print(a)
for i in b:
    if i < 0:
        a.remove(i)
        print(a)
    else:
        continue
print(a)

#
# a =[-1,-15,-4,5,7,-50,-28,9,-8,4,-9,-70]
# for i in a:
#     if i<0:
#         continue
#     else:
#         print(i,end=' ')
#































