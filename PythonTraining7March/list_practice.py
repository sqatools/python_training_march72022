list1 = list()
print(type(list1))
print(list1)


list1 = [2, 4, 5, [4, 7], 'Hello']
"""
-> list follows indexing similar like string
-> list is a mutable data type, it means we can modify it.
-> list is structural data type
"""
"""
# get element from index 0
print(list1[0])

# get element from sublist
print(list1[3][1])

# get specific char from string in the list.
print(list1[4][1])

# slicing in the list.
list2 = [3, 6, 7, 9, 2, 6, 4]

# get element from 3 index to end
output = list2[3:]
print(output)

# get elements from 2 to 6
print(list2[2:6])

# reverse the list
print(list2[::-1])
"""
############################################
# list methods
#print(dir(list))
"""
'append', 'clear', 'copy', 'count', 'extend', 
'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""
"""
############ Add data to the list #############

list3 = list()

# append method : add data to the end of the list
list3.append(4)
list3.append(11)
print(list3)

# insert method : insert data at specific index.
list4 = [5, 7, 9, 3, 6]
list4.insert(3, 44)
print(list4)

# extend method method : add list1 to list2
lista = [2, 5, 8]
listb = ['a', 'b', 'c', 5.8]
listb.extend(lista)

print(listb)
print(lista)


listp = [4, 6, 8]
listq = [6, 8, 2, 9]

#listq.insert(2, listp)

#print(listq)
#print(listq[2][1])

# add list with + operator
listq = listp + listq
print(listq)

print(listp)
print(listq)


####### Remove data from the list ##########
# Remove method : remove specific element from the list

lists = [4, 6, 8, 6, 8, 2, 9]
lists.remove(2)
print(lists)

# pop method : remove element from specific index and return it, default index is -1
listp = [4, 6, 8, 6, 8, 2, 9]
var = listp.pop()
print("listp :", listp)
print(var)


var2 = listp.pop(3)
print(var2)
print("listp :", listp)


# Get index of any element in the list
listpq = [4, 6, 88, 16, 8, 2, 9, 4, 2]

print("index :",listpq.index(2))
print("index :",listpq.index(4))

# get count of any element from the list
count_val = listpq.count(6)
print("count value :", count_val)


# reverse the list: reverse method : this method reverse the list and modify existing list
list11 = [4, 2, 7, 11, 6]
list11.reverse()

print(list11)

list12 = [14, 2, 7, 11, 16]

# reversed : this method reverse the list, but does not modify existing list.
new_list = reversed(list12)
print(new_list)
for val in new_list:
    print(val, end=" ")

print("\nlist12 :",  list12)

# reverse list through the program
list13 = [14, 2, 7, 11, 16, 19]
new_list13 = []

for i in range(-1, -len(list13)-1, -1):
    #print(list13[i], end=" ")
    new_list13.append(list13[i])

print(new_list13)
"""
######################## sorting of the list #################
"""
# sorting of the list : sort method

list33 = [3, 5, 7, 1, 12, 22]

list33.sort()
print(list33)

# reversed method
list44 = [5, 7, 1, 22, 3, 2, 6, 12]
new_list44 = sorted(list44)
print("new_list44:", new_list44)
print("list44 :", list44)

# CLear : clear data from the list
list44.clear()
print("list44 :", list44)
"""
#######################################################
user=['u1','u2','u3']
pass_w=['p1','p2','p3']

User_name=input('Enter your user name : ')

for i in user:
    if i==User_name:
        Pass_w = input('Enter your Password : ')
        for j in pass_w:
            if i==User_name and j==Pass_w:
                print('login successful')
                break
            else:
                print('Wrong Password')
                break
        break

    else:
        print('Wrong User name')
        break














