# Nested loop program
#Program to print given * pattern with the help of nested loop

"""
*
**
***
****
*****
****
***
**
*
"""
"""
pattern = "#"
for i in range(1, 6):
    for j in range(i):
        print(pattern, end=" ")
    print("\n")

for i in range(4, 0, -1):
    for j in range(i):
        print(pattern, end=" ")
    print("\n")

"""


"""
1 

2 3 

4 5 6 

7 8 9 10 

11 12 13 14 15 

16 17 18 19 

20 21 22 

23 24 

25 


"""
"""
temp = 1
for i in range(1, 6):
    for j in range(i):
        print(temp, end=" ")
        temp = temp+1
    print("\n")

for i in range(4, 0, -1):
    for j in range(i):
        print(temp, end=" ")
        temp = temp + 1
    print("\n")
"""


for i in range(1, 6):
    for j in range(i):
        if i%2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print("\n")

for i in range(4, 0, -1):
    for j in range(i):
        if i % 2 == 0:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print("\n")
