str1 = 'Hello'
str2 = 'Good Morning'
print(str1+str2)

print(str1.__add__(str2))

num1 = 40
num2 = 50

print(num1 + num2)
print(num1.__add__(num2))

list1 = [3, 5, 7]
list2 = [6, 8, 3]

print(list1+list2)
print(list1.__add__(list2))

num3 = 6
num4 = 8
print(num3*num4)
print(num3.__mul__(num4))

new_str = 'Hello'

print(new_str.__mul__(num3))