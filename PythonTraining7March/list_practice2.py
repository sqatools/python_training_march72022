"""

list1 = [3, 6, 7, 3, 5, 1, 4]

# 1. Reverse the list by slicing : it does not modify existing list
list_output1 = list1[::-1]
print(list_output1)
print("list1:", list1)

# 2.  reverse the list with the help of reverse method: it modify existing list and reverse the data

list1.reverse()
print("list1 :", list1)

# 3. reverse the list with the help of reversed method. : it does not modify existing list

list2 = [5, 7, 2, 7, 4, 8]

output2 = reversed(list2)
print("output2:", output2)
print("list2:", list2)

for var in output2:
    print(var, end=" ")

#print("__"*40)
# 4 reverse the list with program logic
list3 = [5, 7, 8, 3, 8, 1]
print("\n")
print("__"*40)
list_length = len(list3)
print(list_length)
print(list3[-list_length])

for i in range(-1, -len(list3)-1, -1):
    print(i, ":", list3[i])

##########################################################
list1 = [1, 2, 3, 7, 12, 67, 15, 18, 21, 28]

#output 1 : list of square of all the numbers.
#output2 : list of odd numbers and even numbers
#output3 : list of number which are divide by 3
#          list of number divide by 7
#          list of numbers which are not divide 3 and 7

#Program1 :

lista = [1, 2, 3, 7, 12, 67, 15, 18, 21, 28]
s_list = []

for val in lista:
    sq_var = val**2
    s_list.append(sq_var)

print(s_list)


#output2 : list of odd numbers and even numbers

#output3 : list of number which are divide by 3
#          list of number divide by 7
#          list of numbers which are not divide 3 a

listb = [1, 2, 3, 7, 12, 67, 15, 18, 21, 28]
list_3 = []
list_7 = []
list_no = []

for var in listb:
    if var%3 == 0:
        list_3.append(var)
    elif var%7 == 0:
        list_7.append(var)
    else:
        list_no.append(var)

print("list_3:", list_3)
print("list_7:", list_7)
print("list_no:", list_no)
"""
##############################################

listc = [1, 2, 3, 7, 12, 67, 15, 18, 21, 28]
max_value = max(listc)
min_Value = min(listc)
sun_od_all_numbers = sum(listc)
sum_1 = sum((4, 5))
print(sum_1)


print("max_value :", max_value)
print("min value :", min_Value)
print("sum : ", sun_od_all_numbers)

# remove entire data from memory
del listc
print(listc)









