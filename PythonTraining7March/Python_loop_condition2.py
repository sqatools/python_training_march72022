"""
continue and break
"""

# for i in range(10):
#     if i == 3 or i == 5 or i == 7:
#         continue
#     print(i, ":", i**2)

# for i in range(10):
#     if i == 5:
#         break
#     print(i, ":", i**2)

# While Loop
"""
n = 1

while n < 30:
    print(n)
    n = n + 1
"""

# infinite loop
"""
ab = 1
while True:
    print(ab**2)
    if ab == 50:
        break
    ab = ab + 1
"""

#write a program for calculator which has options to add, sub subtract, multiply, divide
while True:
    print("Please enter your option: \n"
          "1. Addition + \n"
          "2. Multiply * \n"
          "3. Subtraction - \n"
          "4. Divide \ \n")

    user_input = int(input("Select the number from 1 to 4:"))
    print(user_input)
    if user_input in [1, 2, 3, 4]:
        if user_input == 1:
            num1 = int(input("Please enter your first number :"))
            num2 = int(input("Please enter your second number :"))
            print("Addition of two numbers:", num1+num2)

        elif user_input == 2:
            num1 = int(input("Please enter your first number :"))
            num2 = int(input("Please enter your second number :"))
            print("Multiplication of two numbers:", num1*num2)

        elif user_input == 3:
            num1 = int(input("Please enter your first number :"))
            num2 = int(input("Please enter your second number :"))
            print("Subtraction of two numbers:", num1 - num2)

        elif user_input == 4:
            num1 = int(input("Please enter your first number :"))
            num2 = int(input("Please enter your second number :"))
            print("Division of two numbers:", num1 // num2)
    else:
        print("Please enter correct number from 1, 2, 3 & 4")
        break


    print("___"*50)
"""
##################################################################
"""
"""
num = 10
while num > 0:
    print(num)
    num = num -1
else:
    print("Number is less than 0")


for i in range(10, 0, -1):
    print(i)

list1 = [4, 6, 8, 3, 5, 1, 34]

for x in range(len(list1)):
    if list1[x]%2 == 0:
        print(list1[x])
    else:
        continue

for x in list1:
    if x%2 == 0:
        print(x)
    else:
        continue

"""
