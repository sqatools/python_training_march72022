"""
function parameters
"""

def addition(a, b):
    print("a :", a)
    print("b :", b)
    c = a + b
    print(c)

#call by values
#addition(50, 60)

#call by reference
num1 = 50
num2 = 100
#addition(num1, num2)
#addition(num2, num1)


#default value of the paramater
def multiplication(num1, num2, num3=50, num4=60):
    print("num1:", num1)
    print("num2:", num2)
    print("num2:", num3)
    print("num2:", num4)
    output = num1*num2*num3
    print(output)

#multiplication(10)
#multiplication(10, 40)
#multiplication(num2=40) : it will throw error
#multiplication(num2=5, num1=10)
#multiplication(10, 20, num3=30)

def addition_of_numbers(num1 , num2, num3=50, num4=60):
    print("num1:", num1)
    print("num2:", num2)
    print("num2:", num3)
    print("num2:", num4)
    output = num1+num2+num3
    print(output)

addition_of_numbers('a', 'b', 'c', 'd')
addition_of_numbers(12, 23, 34, 45)
addition_of_numbers(2.9, 3.9, 2.3, 4.0)
addition_of_numbers([4, 7], [6, 3], [4, 2], [3, 1])

def addition_of_all_numbers_from_list(list1):
    temp_sum = 0
    for var in list1:
        temp_sum = temp_sum + var

    print(temp_sum)

input_list = [5, 3, 6, 2, 6]
addition_of_all_numbers_from_list(input_list)
