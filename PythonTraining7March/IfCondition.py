"""
if condition:
    code
else:
    code

"""
door = "unlock"


if door == "lock":
    print("Door is locked, can not open")
else:
    print("I can open the door")

"""
Logical operator /conditional operators
var1 = 10
var2 = 20
1) Equal to operator : ==
    var1 == var2
2) Greater than : >    :   var1 > var2
3) Less than : <       :   var1 < var2
4) Greater than : >=   :   var1 >= var2
5) Less than Equal to : <=  : var1 <= var2
6) not equal : !=    : var1 != var2

7) and condition

True and True : True
False and True : False
True and False : False
False and False : False

8) Or Condition

True or True : True
False or True : True
True or False : True
False or False : False

"""
# input : this method take user input as string
#var1 = input("Please enter your input1 :")
#var2 = input("Please enter your input2 :")
#print(var1)
#print(type(var1))

"""
if var1 == var2:
    print("both variables are equal")
else:
    print("variables are not equal ")
"""

# 2) Greater than : >    :   var1 > var2

#var1 = int(input("Please enter your input1 :"))
#var2 = int(input("Please enter your input2 :"))

"""
if var1 > var2:
    print("var1 is greater")
else:
    print("var2 is greater")
"""

# if var1 < var2:
#     print("var2 is greater")
# else:
#     print("var1 is greater")

"""
#if var1 >= var2:
if var1 <= var2:
    print("var2 is greater or equal to var1")
else:
    print("var2 is has less value")
"""


##########################################
# and operator
"""
var1 = 250
var2 = 245
var3 = 225

# if var3 > var1 and var3 > var2:
#     print("var3 has greater value")
# else:
#     print("var3 does not have greater value than var1 and var2")

if var3 > var1 or var3 > var2:
    print("var3 has greater value")
else:
    print("var3 does not have greater value than var1 and var2")
"""


"""
if condition1:
    code block
elif condition2:
    code block
elif condition3:
    code block
else:
    code block
"""
"""
var1 = 301
var2 = 350
var3 = 305

if var1 > var2 and var1 > var3:
    print("var1 has greater value", var1)
elif var2 > var1 and var2 > var3:
    print("var2 has greater value", var2)
elif var3 > var1 and var3 > var2:
    print("var3 has greater value", var3)

"""
#################################################







"""
if condition1:
    if condition2:
        code block
    else:
        code block
else:
    code block
"""

#num = 22

"""
if num%2 == 0:
    print("this is even number", num)
    if num%5 == 0:
        print("this number is divide 5 as well :", num)
        if num%3 == 0:
            print("this number is divide 3 as well :", num)
        else:
            print("this number can not divide by 3:", num)
    else:
        print("this number can not divide by 5 :", num)
else:
    print("this is odd number", num)
"""

#num = 30

# if num%2 ==0 and num%3 == 0 and num%5 ==0:
#     print("we can divide this number by 2, 3, and 5 :", num)
# else:
#     print("we can not divide this number by 2, 3, and 5 :", num)

"""
num = 15
if num%2 ==0 or num%3 == 0 and num%5 ==0:
    print("we can divide this number by 2 or 3 and 5 :", num)
else:
    print("we can not divide this number by 2 or 3 and 5 :", num)
"""
"""
num = 21
if num%2 ==0 and num%3 == 0 or num%5 ==0:
    print("we can divide this number by 2 and 3 or 5 :", num)
else:
    print("we can not divide this number by 2 and 3 or 5 :", num)

"""

num1 = 60
num2 = 50
num3 = 70

if num1 > num2:
    print("num1 is greater than num2")
    if num1 > num3:
        print("num1 is greater than num3")
    else:
        print("num1 is not greater than num2")
else:
    print("num1 is not greater than num2")